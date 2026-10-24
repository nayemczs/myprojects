from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from flask_security import Security, SQLAlchemyUserDatastore
from flask_wtf.csrf import CSRFProtect
from database.models import db as database, User, Role
from core.views import EstateView, AppointmentScheduler
from core.admin import admin
from core.forms import ExtendedLoginForm, FilterForm, ContactForm, AppointmentForm
from core.emails import mail
from settings.settings import APP_CONFIGS


app = Flask(__name__)
for key, value in APP_CONFIGS.items():
    app.config[key] = value
CSRFProtect(app)
database.init_app(app)
user_data_store = SQLAlchemyUserDatastore(database, User, Role)
Security(app, user_data_store, login_form=ExtendedLoginForm)
admin.init_app(app)
mail.init_app(app)


@app.context_processor
def inject_contact_details():
    return {'admin_email': 'some email', 'admin_phone': 'some phone'}


@app.route('/', methods=['GET', 'POST'])
def index():
    # database.create_all()
    # EstateView.generate_dummy_estates()
    if session.get('active_filters'):
        session.pop('active_filters')

    filter_form = FilterForm()
    contact_form = ContactForm()

    if 'contact_form' in request.form:
        AppointmentScheduler.handle_contact_form(contact_form)

    featured_estates = EstateView.featured()
    return render_template(
        'index.html',
        featured_estates=featured_estates,
        filter_form=filter_form,
        contact_form=contact_form
    )


@app.route('/about_us/')
def about_us():
    return render_template('about_us.html')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()

    AppointmentScheduler.handle_contact_form(contact_form)
    return render_template('contact.html', contact_form=contact_form)


@app.route('/appointments/')
def appointments():
    slots = AppointmentScheduler.slots_within_days()
    return render_template('appointments.html', slots=slots)


@app.route('/make_appointment/', methods=['GET', 'POST'])
def make_appointment():
    if request.method == 'GET':
        return redirect(url_for('appointments'))

    if 'slot_id' not in request.form:
        abort(400, description='Bad request.')

    appointment_form = AppointmentForm()
    slot = AppointmentScheduler.get_slot(request.form['slot_id'])
    print(slot, request.form)

    if 'appointment' in request.form:
        if appointment_form.validate_on_submit():
            scheduler = AppointmentScheduler(appointment_form, appointment=True)

            if scheduler.check_slot(appointment_form.slot_id.data):
                if scheduler.send_message():
                    scheduler.book_slot()
                    flash(
                        'Your appointment request has been sent. Please keep an eye on your emails for updates.',
                        'success'
                    )
                    return redirect(url_for('contact'))
                else:
                    flash('Sorry, something went wrong. Make sure you have entered valid email address.', 'error')
            else:
                flash('Sorry, this schedule is no longer available.', 'error')
    return render_template('appointment.html', slot=slot, appointment_form=appointment_form)


@app.route('/listing/', methods=['GET', 'POST'])
def listing():
    page = request.args.get('page', 1, type=int)
    filter_form = FilterForm()
    estate_view = EstateView(current_page=page)
    if filter_form.validate_on_submit():
        active_filters = {
            'search': filter_form.search.data,
            'keyword': filter_form.keyword.data,
            'city': filter_form.city.data,
            'category': filter_form.category.data,
            'offer': filter_form.offer.data,
            'bedrooms': filter_form.bedrooms.data,
            'bathrooms': filter_form.bathrooms.data,
            'space_range_min': filter_form.space_range_min.data,
            'space_range_max': filter_form.space_range_max.data,
            'order_by': filter_form.order_by.data
        }

        session['active_filters'] = active_filters
    else:
        active_filters = session.get('active_filters')

    print(active_filters)
    if active_filters:
        estates = estate_view.apply_filters(active_filters)
    else:
        estates = estate_view.all_estates()

    options = estate_view.all_options()
    return render_template(
        'listing.html',
        filter_form=filter_form,
        estates=estates,
        cities=options['cities'],
        categories=options['categories'],
        bedrooms=options['bedrooms'],
        bathrooms=options['bathrooms'],
        offers=options['offers'],
        orderings=options['orderings']
    )


@app.route('/estate/<int:estate_id>/show/', methods=['GET', 'POST'])
def show(estate_id):
    contact_form = ContactForm()

    AppointmentScheduler.handle_contact_form(contact_form)
    estate = EstateView.get(estate_id)
    return render_template('single_listing.html', estate=estate, contact_form=contact_form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
