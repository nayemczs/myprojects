from flask import flash, redirect
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_admin.babel import gettext
from flask_admin.model.form import InlineFormAdmin
from flask_admin.model.template import macro
from wtforms.fields import PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from database.models import db, Estate, Feature, Featured, Category, Image, City, Offer, AppointmentSlot, User, Role
import logging

log = logging.getLogger("flask-admin.sqla")


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/admin/login/')


class AdminIndex(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/admin/login/')


class CityView(AdminView):
    column_searchable_list = 'name',


class CategoryView(AdminView):
    column_searchable_list = 'name',


class OfferView(AdminView):
    column_searchable_list = 'value',


class AppointmentView(AdminView):
    column_searchable_list = ('date', 'is_booked', 'appointee_email', 'appointee_name')
    column_default_sort = ('date', True)


class ImageView(AdminView):
    edit_template = 'admin/edit.html'
    create_template = 'admin/create.html'
    form_extra_fields = {
        'image': FileField('Upload Image', validators=[FileRequired(), FileAllowed(['png'], 'PNG images Only!')])
    }
    form_widget_args = {
        'name': {'disabled': True},
        'link': {'disabled': True}
    }
    column_searchable_list = ('estate.title', 'link')
    column_labels = {
        'name': 'Image'
    }
    column_formatters = {
        'name': macro('render_image')
    }

    def create_model(self, form):
        image = self.model()
        try:
            form.populate_obj(image)
            image.add_file(form.image.data)
            self.session.add(image)
            self._on_model_change(form, image, True)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to update record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to update record.')
            self.session.rollback()
            return False
        else:
            self.after_model_change(form, image, True)

        return image

    def update_model(self, form, image):
        try:
            form.populate_obj(image)
            image.add_file(form.image.data)
            self.session.add(image)
            self._on_model_change(form, image, False)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to update record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to update record.')

            self.session.rollback()
            return False
        else:
            self.after_model_change(form, image, False)

        return True

    def delete_model(self, image):
        try:
            self.on_model_delete(image)
            image.delete()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to delete record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to delete record.')

            self.session.rollback()

            return False
        else:
            self.after_model_delete(image)

        return True


class InlineImageView(InlineFormAdmin):
    edit_template = 'admin/edit.html'
    create_template = 'admin/create.html'
    form_extra_fields = {
        'image': FileField('Upload Image', validators=[FileAllowed(['png'], 'PNG images Only!')])
    }
    form_widget_args = {
        'name': {'disabled': True},
        'link': {'disabled': True}
    }

    def on_model_change(self, form, image, is_created):
        if form.image.data is not None:
            image.add_file(form.image.data)


class EstateView(AdminView):
    edit_template = 'admin/edit.html'
    create_template = 'admin/create.html'
    inline_models = (InlineFormAdmin(Feature), InlineFormAdmin(Featured), InlineImageView(Image))
    form_extra_fields = {
        'image': FileField('Upload Image', validators=[FileAllowed(['png'], 'PNG images Only!')])
    }
    form_widget_args = {
        'image_name': {'disabled': True},
        'image_link': {'disabled': True}
    }
    column_searchable_list = ('title', 'location', 'city.name', 'offer.value')
    column_exclude_list = 'image_name',
    column_labels = {
        'image_link': 'Image'
    }
    column_formatters = {
        'image_link': macro('render_estate_image')
    }

    def create_model(self, form):
        estate = self.model(
            title=form.title.data,
            location=form.location.data,
            description=form.description.data,
            price=form.price.data,
            area=form.area.data,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data
        )
        try:
            form.populate_obj(estate)
            if form.image.data:
                estate.save_image(form.image.data)
            self.session.add(estate)
            self._on_model_change(form, estate, True)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to update record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to update record.')
            self.session.rollback()
            return False
        else:
            self.after_model_change(form, estate, True)

        return estate

    def update_model(self, form, estate):
        try:
            form.populate_obj(estate)
            if form.image.data:
                estate.save_image(form.image.data)
            self.session.add(estate)
            self._on_model_change(form, estate, False)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to update record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to update record.')

            self.session.rollback()
            return False
        else:
            self.after_model_change(form, estate, False)

        return True

    def delete_model(self, estate):
        try:
            self.on_model_delete(estate)
            estate.delete()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to delete record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to delete record.')

            self.session.rollback()

            return False
        else:
            self.after_model_delete(estate)

        return True


class UserView(AdminView):
    edit_template = 'admin/edit.html'
    create_template = 'admin/create.html'
    inline_models = InlineImageView(Role),
    form_excluded_columns = ('password', 'confirmed_at')
    form_extra_fields = {
        'new_password': PasswordField(
            'New Password',
            validators=[DataRequired(), Length(min=6), EqualTo('confirm_pass')]
        ),
        'confirm_pass': PasswordField(
            'Confirm Password',
            validators=[DataRequired(), Length(min=6)]
        )
    }
    column_searchable_list = ('first_name', 'last_name', 'email')

    def create_model(self, form):
        user = self.model(
            email=form.email.data,
            password=form.new_password.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            is_active=form.is_active.data,
            is_admin=form.is_admin.data
        )
        try:
            form.populate_obj(user)
            self.session.add(user)
            self._on_model_change(form, user, True)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to update record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to update record.')
            self.session.rollback()
            return False
        else:
            self.after_model_change(form, user, True)

        return user

    def update_model(self, form, user):
        try:
            form.populate_obj(user)
            user.set_password(form.new_password.data)
            self.session.add(user)
            self._on_model_change(form, user, False)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to update record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to update record.')

            self.session.rollback()
            return False
        else:
            self.after_model_change(form, user, False)

        return True


admin = Admin(index_view=AdminIndex())
admin.add_view(CategoryView(Category, db.session))
admin.add_view(CityView(City, db.session))
admin.add_view(EstateView(Estate, db.session))
admin.add_view(OfferView(Offer, db.session))
admin.add_view(AdminView(Featured, db.session))
admin.add_view(AdminView(Feature, db.session))
admin.add_view(ImageView(Image, db.session))
admin.add_view(AppointmentView(AppointmentSlot, db.session))
admin.add_view(UserView(User, db.session))
admin.add_view(AdminView(Role, db.session))
admin.add_link(MenuLink(name='Logout', class_name='logout_button', url='/admin/logout/'))
