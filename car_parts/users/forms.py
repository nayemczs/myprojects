from django.forms import Form, ModelForm, CharField, PasswordInput, ImageField, EmailField
from django.core.validators import (
    MinLengthValidator,
    FileExtensionValidator,
    validate_image_file_extension,
    EmailValidator
)
from django.utils.translation import gettext_lazy as _
from .models import User


class RegistrationForm(ModelForm):
    first_name = CharField(validators=[MinLengthValidator(4)])
    last_name = CharField(validators=[MinLengthValidator(4)])
    address = CharField(validators=[MinLengthValidator(6)])
    confirm_password = CharField(widget=PasswordInput, validators=[MinLengthValidator(8)])
    image = ImageField(validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg']),
        validate_image_file_extension
    ])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'email', 'password', 'confirm_password', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'] = CharField(widget=PasswordInput, validators=[MinLengthValidator(8)])
        self.fields['email'].widget.attrs.update({'class': 'input100', 'placeholder': 'E-mail Address'})
        self.fields['password'].widget.attrs.update({'class': 'input100', 'placeholder': 'Password'})

    first_name.widget.attrs.update({'class': 'input100', 'placeholder': 'First Name'})
    last_name.widget.attrs.update({'class': 'input100', 'placeholder': 'Last Name'})
    address.widget.attrs.update({'class': 'input100', 'placeholder': 'Address'})
    confirm_password.widget.attrs.update({'class': 'input100', 'placeholder': 'Confirm Password'})
    image.widget.attrs.update({'class': 'input100', 'placeholder': 'Upload Image'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmation = cleaned_data.get('confirm_password')

        if password and password != confirmation:
            self.add_error('password', _('Password does NOT match with the confirmation field'))


class VendorRegistrationForm(ModelForm):
    name = CharField(validators=[MinLengthValidator(4)])
    region = CharField(validators=[MinLengthValidator(3)])
    country = CharField(validators=[MinLengthValidator(3)])
    city = CharField(validators=[MinLengthValidator(3)])
    address = CharField(validators=[MinLengthValidator(6)])
    confirm_password = CharField(widget=PasswordInput, validators=[MinLengthValidator(8)])
    image = ImageField(validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg']),
        validate_image_file_extension
    ])

    class Meta:
        model = User
        fields = ['name', 'email', 'region', 'country', 'city', 'address', 'password', 'confirm_password', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'] = CharField(widget=PasswordInput, validators=[MinLengthValidator(8)])
        self.fields['email'].widget.attrs.update({'class': 'input100', 'placeholder': 'E-mail Address'})
        self.fields['password'].widget.attrs.update({'class': 'input100', 'placeholder': 'Password'})

    name.widget.attrs.update({'class': 'input100', 'placeholder': 'Company Name'})
    region.widget.attrs.update({'class': 'input100', 'placeholder': 'Region'})
    country.widget.attrs.update({'class': 'input100', 'placeholder': 'Country'})
    city.widget.attrs.update({'class': 'input100', 'placeholder': 'City'})
    address.widget.attrs.update({'class': 'input100', 'placeholder': 'Address'})
    confirm_password.widget.attrs.update({'class': 'input100', 'placeholder': 'Confirm Password'})
    image.widget.attrs.update({'class': 'input100', 'placeholder': 'Upload Image'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmation = cleaned_data.get('confirm_password')

        if password and password != confirmation:
            self.add_error('password', _('Password does NOT match with the confirmation field'))


class LoginForm(Form):
    username = EmailField(validators=[EmailValidator()])
    password = CharField(widget=PasswordInput, validators=[MinLengthValidator(8)])

    username.widget.attrs.update({'class': 'input100', 'placeholder': 'Email'})
    password.widget.attrs.update({'class': 'input100', 'placeholder': 'Password'})
