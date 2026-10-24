from django.contrib.admin import register, ModelAdmin
from django.contrib.admin.helpers import AdminForm
from django.urls import path
from django.shortcuts import redirect
from .models import PageBanner, Brand, Colour, Watch
from .forms import PageBannerForm, BrandForm, ColourForm, WatchForm, UploadJSONForm


# Register your models here.
class URLKeyAdminInterface:

    def save_model(self, request, obj, form, change):
        url_key = form.cleaned_data.get('url_key')
        if url_key:
            obj.url_key = url_key
        return super().save_model(request, obj, form, change)


class BaseAdmin(URLKeyAdminInterface, ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'url_key']


@register(PageBanner)
class PageBanner(ModelAdmin):
    exclude = ['page']
    form = PageBannerForm

    def save_model(self, request, obj, form, change):
        _return = super().save_model(request, obj, form, change)
        if change and form.has_changed():
            for item in form.old_images:
                if item['name']:
                    obj.remove_image(image_var=item['image_var'], image_name=item['name'])
        return _return

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@register(Brand)
class BrandAdmin(BaseAdmin):
    form = BrandForm

    def save_model(self, request, obj, form, change):
        _return = super().save_model(request, obj, form, change)
        if change and form.has_changed():
            for item in form.old_images:
                if item['name']:
                    obj.remove_image(image_var=item['image_var'], image_name=item['name'])
        return _return


@register(Colour)
class ColourAdmin(BaseAdmin):
    form = ColourForm


@register(Watch)
class WatchAdmin(BaseAdmin):
    form = WatchForm

    def get_urls(self):
        return [
            path('upload_json/', self.admin_site.admin_view(self.upload_json_view), name='upload_json')
        ] + super().get_urls()

    def upload_json_view(self, request):
        form = UploadJSONForm(request.POST or None, request.FILES or None)
        fields = ['json_file']

        if form.is_valid():
            watches = form.cleaned_data['json_data']['watches']
            for data in watches:
                data['brand'] = self.model.parse_brand(data.get('brand'))
                data['colour'] = self.model.parse_colour(data.get('colour'))
                watch = self.model(**data)
                watch.generate_and_update_url_key()
            self.message_user(request, 'JSON uploaded Successfully.')
            return redirect('admin:pages_watch_changelist')

        context = {
            **self.admin_site.each_context(request),
            'title': 'Upload JSON',
            'adminform': AdminForm(form, [(None, {'fields': fields})], {}, model_admin=self),
            'inline_admin_formsets': [],
            'show_save_and_add_another': False,
            'show_save_and_continue': False
        }
        return self.render_change_form(request, context, add=True)
