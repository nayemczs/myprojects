"""
Authors: TANZIM AHMED and NAYEMUL ISLAM MAJUMDER
Author Emails: tanzim.din@northsouth.edu and nayemul.majumder@northsouth.edu
Created on: 25th July 2020
For: hunchgroup.com
"""


from flask import render_template, flash, abort
from .emails import EmailServices
from database.models import Estate, Feature, City, Category, Offer, AppointmentSlot, Featured, Image
from settings.settings import ADMIN_EMAIL
from random import randint
from datetime import date, timedelta, datetime


class EstateView:
    estate_class = Estate
    feature_class = Feature
    is_featured_class = Featured
    city_class = City
    category_class = Category
    offer_class = Offer

    def __init__(self, current_page=1):
        self.per_page = 9
        self.current_page = current_page
        self.query = self.estate_class.query
        self.filters = None
        self.min_area = 120
        self.max_area = 820

    def apply_filters(self, filters):
        if filters is None:
            raise Exception('Filters required')
        self.filters = filters

        return self.build_query().paginate(page=self.current_page, per_page=self.per_page)

    def build_query(self):
        if self.filters['city']:
            self.query = self.query.filter_by(city_id=self.filters['city'])
        if self.filters['category']:
            self.query = self.query.filter_by(category_id=self.filters['category'])
        if self.filters['offer']:
            self.query = self.query.filter_by(offer_id=self.filters['offer'])
        if self.filters['bedrooms']:
            if self.filters['bedrooms'] == '5+':
                self.query = self.query.filter(self.estate_class.bedrooms >= 5)
            else:
                self.query = self.query.filter_by(bedrooms=self.filters['bedrooms'])
        if self.filters['bathrooms']:
            if self.filters['bathrooms'] == '5+':
                self.query = self.query.filter(self.estate_class.bathrooms >= 5)
            else:
                self.query = self.query.filter_by(bathrooms=self.filters['bathrooms'])
        if self.filters['space_range_min'] and self.filters['space_range_min'] != self.min_area:
            self.query = self.query.filter(self.estate_class.area >= self.filters['space_range_min'])
        if self.filters['space_range_max'] and self.filters['space_range_max'] != self.max_area:
            self.query = self.query.filter(self.estate_class.area <= self.filters['space_range_max'])
        if self.filters['keyword']:
            self.query = self.query.join(self.estate_class.features)\
                .filter(self.feature_class.name.like(f"%{self.filters['keyword']}%"))
        if self.filters['search']:
            self.query = self.query.join(
                self.estate_class.features,
                self.estate_class.city,
                self.estate_class.category
            ).filter(
                self.estate_class.title.like(f"%{self.filters['search']}%") |
                self.estate_class.description.like(f"%{self.filters['search']}%") |
                self.estate_class.location.like(f"%{self.filters['search']}%") |
                self.feature_class.name.like(f"%{self.filters['search']}%") |
                self.city_class.name.like(f"%{self.filters['search']}%") |
                self.category_class.name.like(f"%{self.filters['search']}%")
            )
        if self.filters['order_by']:
            if self.filters['order_by'] == '1':
                self.query = self.query.order_by(self.estate_class.date_added.desc())
            elif self.filters['order_by'] == '2':
                self.query = self.query.order_by(self.estate_class.price.asc())
            elif self.filters['order_by'] == '3':
                self.query = self.query.order_by(self.estate_class.price.desc())

        return self.query

    def all_estates(self):
        return self.query.paginate(page=self.current_page, per_page=self.per_page)

    @classmethod
    def get(cls, estate_id):
        return cls.estate_class.query.get(estate_id)

    @classmethod
    def featured(cls):
        return cls.estate_class.query.join(cls.estate_class.featured).filter(cls.is_featured_class.id is not None).all()

    @classmethod
    def all_options(cls):
        options = {
            'cities': cls.city_class.query.all(),
            'categories': cls.category_class.query.all(),
            'bedrooms': ['0', '1', '2', '3', '4', '5+'],
            'bathrooms': ['0', '1', '2', '3', '4', '5+'],
            'offers': cls.offer_class.query.all(),
            'orderings': [
                {
                    'id': 1,
                    'text': 'Newest'
                },
                {
                    'id': 2,
                    'text': 'Price (Low to High)'
                },
                {
                    'id': 3,
                    'text': 'Price (High to Low)'
                }
            ]
        }
        return options

    @classmethod
    def generate_dummy_estates(cls, count=50):
        feature_options = [
            'Gated Community',
            'Window Shutters',
            'Heated Floors',
            'Fireplace',
            'Automatic Sprinklers',
            'Ocean Views',
            'Private Patio',
            'Beach Access',
            'Rooftop Terrace'
        ]
        for i in range(1, count+1):
            estate = cls.estate_class(
                title=None,
                location=f'Road {randint(1000, 9999)}, no.{randint(100, 999)}',
                description='Integer nec bibendum lacus. Suspendisse dictum enim sit amet libero malesuada.',
                price=randint(5000, 999999),
                area=randint(120, 820),
                bedrooms=randint(1, 10),
                bathrooms=randint(1, 10)
            )
            estate.city_id = randint(1, 5)
            offer_id = randint(0, 4)
            if offer_id > 0:
                estate.offer_id = offer_id
            estate.category_id = randint(1, 5)
            feature_list = []
            image_list = []
            for j in range(randint(0, 9)):
                feature_list.append(Feature(name=feature_options[j]))
            for j in range(randint(0, 5)):
                image_list.append(Image())
            estate.features = feature_list
            estate.images = image_list
            estate.title = f'{cls.category_class.query.get(estate.category_id).name} ' \
                           f'in {cls.city_class.query.get(estate.city_id).name}'
            estate.save()

    @classmethod
    def all(cls):
        return cls.estate_class.query.all()


class AppointmentScheduler:
    slot_class = AppointmentSlot
    admin_email = ADMIN_EMAIL
    message = None
    slot = None
    is_checked = False

    def __init__(self, form, appointment=False):
        self.appointment = appointment
        self.user_name = form.name.data.title()
        self.user_email = form.email.data
        self.contact_no = form.contact_no.data
        if appointment:
            self.user_text_template = 'email/user_appointment_template.txt'
            self.user_html_template = 'email/user_appointment_template.html'
            self.admin_text_template = 'email/admin_appointment_template.txt'
            self.admin_html_template = 'email/admin_appointment_template.html'
        else:
            self.user_text_template = 'email/user_contact_template.txt'
            self.user_html_template = 'email/user_contact_template.html'
            self.admin_text_template = 'email/admin_contact_template.txt'
            self.admin_html_template = 'email/admin_contact_template.html'
            self.message = form.text.data

    def send_message(self):
        if self.appointment and self.slot is None:
            return False
        return self.notify_user() and self.notify_admin()

    def book_slot(self):
        if not self.is_checked:
            abort(400, description='Invalid request.')

        self.slot.appointee_name = self.user_name
        self.slot.appointee_email = self.user_email
        self.slot.appointee_contact_no = self.contact_no
        self.slot.is_booked = True
        self.slot.save()

    def notify_admin(self):
        if self.appointment:
            subject = 'New Appointment'
            text_content = render_template(self.admin_text_template, name=self.user_name, slot=self.slot)
            html_content = render_template(self.admin_html_template, name=self.user_name, slot=self.slot)
        else:
            subject = 'Contact Request'
            text_content = render_template(self.admin_text_template, name=self.user_name, message=self.message)
            html_content = render_template(self.admin_html_template, name=self.user_name, message=self.message)

        email_service = EmailServices.get_default_service()
        email_service.set_message(
            subject=subject,
            recipients=self.admin_email,
            text_content=text_content,
            html_content=html_content,
            reply_to=self.user_email
        )
        return email_service.send()

    def notify_user(self):
        if self.appointment:
            subject = 'Real Estate New Appointment'
            text_content = render_template(self.user_text_template, name=self.user_name, slot=self.slot)
            html_content = render_template(self.user_html_template, name=self.user_name, slot=self.slot)
        else:
            subject = 'Real Estate Contact Request'
            text_content = render_template(self.user_text_template, name=self.user_name, message=self.message)
            html_content = render_template(self.user_html_template, name=self.user_name, message=self.message)

        email_service = EmailServices.get_default_service()
        email_service.set_message(
            subject=subject,
            recipients=self.user_email,
            text_content=text_content,
            html_content=html_content,
            reply_to=self.admin_email
        )
        return email_service.send()

    def check_slot(self, slot_id):
        self.slot = self.slot_class.query.get(slot_id)
        self.is_checked = (((self.slot.date > date.today()) or
                            ((self.slot.date == date.today()) and (self.slot.start_time > datetime.now().time()))) and
                           not self.slot.is_booked)
        return self.is_checked

    @classmethod
    def get_slot(cls, slot_id):
        cls.slot = cls.slot_class.query.get(slot_id)
        return cls.slot

    @classmethod
    def handle_contact_form(cls, form):
        if form.validate_on_submit():
            scheduler = cls(form)
            if scheduler.send_message():
                flash('Your query has been sent. Please keep an eye on your emails for updates.', 'success')
            else:
                flash('Sorry, something went wrong. Make sure you have entered valid email address.', 'error')

    @classmethod
    def slots_within_days(cls, days=7):
        today = date.today()
        upto = today + timedelta(days=days)
        print(today, upto)
        return cls.slot_class.query.filter_by(is_booked=False)\
            .filter(cls.slot_class.date >= today).filter(cls.slot_class.date <= upto)\
            .order_by(cls.slot_class.date.asc()).all()
