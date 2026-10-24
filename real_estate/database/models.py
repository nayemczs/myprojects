from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
from flask_security.utils import hash_password
from sqlalchemy import event
from settings.settings import BASE_DIR
from datetime import datetime
import os

db = SQLAlchemy()


class EntityInterface:
    id = None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class User(db.Model, UserMixin, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    confirmed_at = db.Column(db.DateTime())
    is_active = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, password, first_name, last_name, is_active=False, is_admin=False):
        self.email = email
        self.password = hash_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = hash_password(password)

    def __str__(self):
        return f'({self.id}) {self.first_name} {self.last_name}'


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return f'({self.id}) {self.name}'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'({self.id}) {self.name}'


class City(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f'({self.id}) {self.name}'


class Estate(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text(10000))
    price = db.Column(db.Float, nullable=False)
    area = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Integer, default=0, nullable=False)
    bathrooms = db.Column(db.Integer, default=0, nullable=False)
    date_added = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    image_name = db.Column(db.String(50), default='default.png', nullable=False)
    image_link = db.Column(db.String(255), default='/static/images/default.png', nullable=False)
    features = db.relationship('Feature', backref='estate')
    images = db.relationship('Image', backref='estate')
    category = db.relationship('Category', uselist=False)
    city = db.relationship('City', uselist=False)
    offer = db.relationship('Offer', uselist=False)

    def __init__(self, title, location, description, price, area, bedrooms, bathrooms):
        self.title = title
        self.location = location
        self.description = description
        self.price = price
        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def save_image(self, image):
        if self.id is None:
            db.session.add(self)
            db.session.flush()
            db.session.refresh(self)

        self.image_name = f'estate_{self.id}.png'
        self.image_link = f'/static/images/{self.image_name}'
        image.save(os.path.join(BASE_DIR, 'static', 'images', self.image_name))

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        if self.image_name != 'default.png':
            try:
                os.remove(os.path.join(BASE_DIR, 'static', 'images', self.image_name))
            except IOError:
                pass

    def __str__(self):
        return f'({self.id}) {self.title}'


class Offer(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f'({self.id}) {self.value}'


class Feature(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    estate_id = db.Column(db.Integer, db.ForeignKey('estate.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f'({self.id}) {self.name}'


class Featured(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    estate_id = db.Column(db.Integer, db.ForeignKey('estate.id', ondelete='CASCADE'), nullable=False, unique=True)
    estate = db.relationship('Estate', backref='featured', uselist=False)

    def __str__(self):
        return f'({self.id}) Featured'


class Image(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), default='default.png', nullable=False)
    link = db.Column(db.String(255), default='/static/images/default.png', nullable=False)
    estate_id = db.Column(db.Integer, db.ForeignKey('estate.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, name=None):
        self.name = name

    def add_file(self, image):
        if self.id is None:
            db.session.add(self)
            db.session.flush()
            db.session.refresh(self)

        self.name = f'image_{self.id}.png'
        self.link = f'/static/images/{self.name}'
        image.save(os.path.join(BASE_DIR, 'static', 'images', self.name))

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        self.delete_image()

    def delete_image(self):
        if self.name != 'default.png':
            try:
                os.remove(os.path.join(BASE_DIR, 'static', 'images', self.name))
            except IOError:
                pass

    def __str__(self):
        return f'({self.id}) {self.name}'


class AppointmentSlot(db.Model, EntityInterface):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    is_booked = db.Column(db.Boolean, default=False, nullable=False)
    appointee_email = db.Column(db.String(255))
    appointee_name = db.Column(db.String(255))
    appointee_contact_no = db.Column(db.String(40))

    __table_args__ = db.UniqueConstraint('date', 'start_time', 'end_time'),


# Image delete event
@event.listens_for(Image, 'after_delete')
def receive_after_delete(mapper, connection, target):
    print('Deleting', target)
    target.delete_image()
