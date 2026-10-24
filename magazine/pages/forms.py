from django.forms import Form, ModelForm, ImageField, ClearableFileInput, CharField, MultipleHiddenInput
from django.core.validators import FileExtensionValidator, validate_image_file_extension
from .models import Place, Region, Destination, Hotel, House, Landscape, Interest, Land
from magazine.exceptions import UrlKeyExistsException


class URLKeyFormInterface:

    def update_key(self):
        if 'name' in self.changed_data:
            name = self.cleaned_data.get('name')
            try:
                url_key = self.Meta.model.generate_url_key(name)
            except UrlKeyExistsException as error:
                if self.instance and self.instance.url_key != error.url_key:
                    self.add_error(
                        'name',
                        'URL key already exists. Please change your name text to have an Unique URL key.'
                    )
            else:
                self.cleaned_data.update({'url_key': url_key})


class BasicArticleForm(ModelForm, URLKeyFormInterface):

    class Media:
        css = {'all': ('css/admin_ck_editor.css',)}
        js = (
            'https://cdn.jsdelivr.net/npm/js-cookie@rc/dist/js.cookie.min.js',
            'ck_editor/build/ckeditor.js',
            'scripts/admin_ck_editor.js'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cover_image'] = ImageField(
            widget=ClearableFileInput,
            validators=[
                FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
                validate_image_file_extension
            ]
        )

    def clean(self):
        super().clean()
        if self.has_changed():
            self.update_key()

            if 'location' in self.changed_data:
                location = self.cleaned_data.get('location')

                if location:
                    print('location changed')


class PlaceForm(BasicArticleForm):

    class Meta:
        model = Place
        fields = '__all__'


class RegionForm(BasicArticleForm):

    class Meta:
        model = Region
        fields = '__all__'


class DestinationForm(BasicArticleForm):

    class Meta:
        model = Destination
        fields = '__all__'


class HotelForm(BasicArticleForm):

    class Meta:
        model = Hotel
        fields = '__all__'


class HouseForm(BasicArticleForm):

    class Meta:
        model = House
        fields = '__all__'

    def clean(self):
        return


class LandscapeForm(ModelForm, URLKeyFormInterface):

    class Meta:
        model = Landscape
        fields = '__all__'

    def clean(self):
        super().clean()
        if self.has_changed():
            self.update_key()


class InterestForm(ModelForm, URLKeyFormInterface):

    class Meta:
        model = Interest
        fields = '__all__'

    def clean(self):
        super().clean()
        if self.has_changed():
            self.update_key()


class LandForm(ModelForm, URLKeyFormInterface):

    class Meta:
        model = Land
        fields = '__all__'

    def clean(self):
        super().clean()
        if self.has_changed():
            self.update_key()


class MultipleCharField(CharField):

    def clean(self, value):
        cleaned = super().clean(value)

        cleaned_value = []
        for value in cleaned.strip('[').strip(']').split(', '):
            value = value.strip("'")
            if value:
                try:
                    value = int(value)
                except ValueError:
                    pass
                cleaned_value.append(value)
        return cleaned_value


class HotelFilterForm(Form):
    hotel_types = MultipleCharField(widget=MultipleHiddenInput, required=False)
    regions = MultipleCharField(widget=MultipleHiddenInput, required=False)
    facilities = MultipleCharField(widget=MultipleHiddenInput, required=False)


class HouseFilterForm(Form):
    house_types = MultipleCharField(widget=MultipleHiddenInput, required=False)
    regions = MultipleCharField(widget=MultipleHiddenInput, required=False)
    conditions = MultipleCharField(widget=MultipleHiddenInput, required=False)
    facilities = MultipleCharField(widget=MultipleHiddenInput, required=False)


class SearchForm(Form):
    city = CharField(required=False)
