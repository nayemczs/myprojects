from django.core.validators import FileExtensionValidator, validate_image_file_extension
from django.forms import (
    Form, ModelForm, CharField, ChoiceField, FileField, ImageField, IntegerField, MultipleHiddenInput, HiddenInput
)
from .models import PageBanner, Brand, Colour, Watch
from thilter.exceptions import UrlKeyExistsException
from thilter.interfaces import URLKeyFormInterface
from thilter.utils import Genders, PriceSort
from json import loads as load_json


class BaseModelForm(URLKeyFormInterface, ModelForm):
    pass


class ModelFormWithImages(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_vars = self.Meta.model.image_vars
        for image_var in self.image_vars:
            self.fields[image_var] = ImageField(required=False, validators=[
                FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg']),
                validate_image_file_extension
            ])
        self.old_images = []

    def clean(self):
        super().clean()

        for image_var in self.image_vars:
            if self.instance.id and image_var in self.changed_data:
                self.old_images.append({
                    'image_var': image_var,
                    'name': self.instance.__getattribute__(image_var).name
                })


class PageBannerForm(ModelFormWithImages):

    class Meta:
        model = PageBanner
        fields = '__all__'


class BrandForm(BaseModelForm):

    class Meta:
        model = Brand
        fields = '__all__'


class ColourForm(BaseModelForm):

    class Meta:
        model = Colour
        fields = '__all__'


class WatchForm(BaseModelForm):

    class Meta:
        model = Watch
        fields = '__all__'


class UploadJSONForm(Form):
    json_file = FileField(label='JSON File', validators=[FileExtensionValidator(['json'])])

    def clean(self):
        """
        Validate JSON file and return watches list.
        """

        super().clean()
        json_data = load_json(self.cleaned_data['json_file'].file.read())
        watches = json_data.get('watches')

        if not watches:
            self.add_error('json_file', "JSON file must contain 'watches' list.")
            return

        valid_keys = Watch.get_field_names()
        validate_unique = Watch.generate_url_key
        invalid_keys = set()
        unique_watches = []

        try:
            for watch in watches:
                for key in watch.keys():
                    # Check if key is valid
                    if key not in valid_keys:
                        invalid_keys.add(key)

                # Check if required fields are valid
                name = watch.get('name')
                if name:
                    try:
                        url_key = validate_unique(name)
                        if unique_watches.count(url_key):
                            raise ValueError
                        unique_watches.append(url_key)
                    except (UrlKeyExistsException, ValueError):
                        self.add_error('json_file', f'Watch: {name} already exists.')
                else:
                    self.add_error('json_file', f'Watch data must contain name attribute.')

                gender = watch.get('gender')
                if gender and gender not in Genders.values:
                    self.add_error('json_file', f'Watch: {name} contains invalid value for gender.')

            # Raise errors for invalid keys
            for key in list(invalid_keys):
                self.add_error('json_file', f"Attribute Error: '{key}' is not a valid attribute.")
        except AttributeError:
            self.add_error('json_file', "Could not parse 'watches' list.")
            return

        self.cleaned_data.update({'json_data': json_data})


class MultiStringField(CharField):

    def clean(self, value):
        cleaned_data = super().clean(value)
        if cleaned_data:
            return load_json(cleaned_data.replace('\'', '"'))
        return ''


class FilterForm(Form):
    brands = MultiStringField(widget=MultipleHiddenInput, required=False)
    price_sort = ChoiceField(choices=PriceSort.choices, widget=HiddenInput, required=False)
    min_price = IntegerField(widget=HiddenInput, required=False)
    max_price = IntegerField(widget=HiddenInput, required=False)
    colours = MultiStringField(widget=MultipleHiddenInput, required=False)
    functions = MultiStringField(widget=MultipleHiddenInput, required=False)
    deliveries = MultiStringField(widget=MultipleHiddenInput, required=False)


class SearchForm(Form):
    text = CharField(widget=HiddenInput, required=False)
