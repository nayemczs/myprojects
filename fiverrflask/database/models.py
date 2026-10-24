from flask import abort
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
from datetime import datetime
from settings.settings import MEDIA_URL


db = SQLAlchemy()

roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")),
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship(
        "Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic")
    )

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_audio(self, audio_id):
        audio = self.audios.filter_by(id=audio_id).first()
        if audio is None:
            abort(404, description='Audio not found.')
        return audio


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))


class Audio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    file_name = db.Column(db.String(75), unique=True, nullable=False)
    link = db.Column(db.String(255), unique=True, nullable=False)
    cursor_position = db.Column(db.Float, default=0, nullable=False)
    is_listened = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('audios', lazy='dynamic'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.link = f'{MEDIA_URL}/{file_name}'

    def delete(self):
        db.session.delete(self)
        db.session.commit()
