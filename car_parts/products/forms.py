from django.forms import Form, ModelForm, CharField, ImageField, ClearableFileInput
from django.core.validators import MinLengthValidator, FileExtensionValidator, validate_image_file_extension
from django.utils.translation import gettext_lazy as _
from .models import Product, Resource


class ProductForm(ModelForm):
    images = ImageField(
        widget=ClearableFileInput,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg']),
            validate_image_file_extension
        ]
    )

    class Meta:
        model = Product
        fields = ['model_name', 'part_name', 'description', 'price', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model_name'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Model Name')}
        )
        self.fields['part_name'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Part Name')}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Description')}
        )
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Price')}
        )
        self.fields['quantity'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Quantity')}
        )

    images.widget.attrs.update(
        {'class': 'form-control custom_option', 'placeholder': _('Images'), 'multiple': True}
    )


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['model_name', 'part_name', 'description', 'price', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model_name'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Model Name')}
        )
        self.fields['part_name'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Part Name')}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Description')}
        )
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Price')}
        )
        self.fields['quantity'].widget.attrs.update(
            {'class': 'form-control custom_option', 'placeholder': _('Quantity')}
        )


class SearchForm(Form):
    part_name = CharField(validators=[MinLengthValidator(2, message=_('You must select a Part'))])
    model_name = CharField(validators=[MinLengthValidator(2, message=_('You must select a Model'))])
    area = CharField(validators=[MinLengthValidator(5, message=_('You must select an Area'))])


class ImageForm(ModelForm):
    class Meta:
        model = Resource
        fields = ['image']
