from re import sub as re_sub
from .exceptions import UrlKeyExistsException


# URL Key Interfaces
class URLKeyInterface:
    """
    Use this to generate unique URL keys for a model whenever the url_key_field is updated.
    """

    url_key = None
    url_key_field = 'name'

    @classmethod
    def generate_url_key(cls, value: str, validate_unique=True) -> str:
        key = re_sub(r'[\W_]+', '-', value.lower())
        key = re_sub('-$', '', key)

        if validate_unique:
            try:
                cls.objects.get(url_key=key)
            except cls.DoesNotExist:
                pass
            else:
                raise UrlKeyExistsException(url_key=key)
        return key

    def generate_and_update_url_key(self) -> str:
        self.url_key = self.generate_url_key(self.get_key_field())
        self.save()
        return self.url_key

    def get_key_field(self):
        return self.__getattribute__(self.url_key_field)

    @property
    def search_key(self) -> str:
        return self.url_key


class URLKeyFormInterface:
    """
    Use this to generate unique URL keys for a model whenever the url_key_field is updated.
    """

    url_key_field = 'name'

    def clean(self):
        super().clean()
        self.update_url_key()

    def update_url_key(self):
        if self.url_key_field in self.changed_data:
            value = self.cleaned_data.get(self.url_key_field)
            try:
                url_key = self.Meta.model.generate_url_key(value)
            except UrlKeyExistsException as error:
                if self.instance and self.instance.url_key != error.url_key:
                    self.add_error(
                        self.url_key_field,
                        f'URL key already exists. Please change {self.url_key_field} text to have an Unique URL key.'
                    )
            else:
                self.cleaned_data.update({'url_key': url_key})

            self.cleaned_data.update({self.url_key_field: value.title()})


class URLKeyAdminInterface:

    def save_model(self, request, obj, form, change):
        url_key = form.cleaned_data.get('url_key')
        if url_key:
            obj.url_key = url_key
        return super().save_model(request, obj, form, change)
