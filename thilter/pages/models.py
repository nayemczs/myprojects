from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from thilter.interfaces import URLKeyInterface
from thilter.utils import Currencies, Genders, PriceSort, Pages
from json import loads as load_json
from secrets import token_urlsafe


# Create your models here.
def upload_directory(instance, file_name):
    if isinstance(instance, PageBanner):
        root = 'banners'
    elif isinstance(instance, Brand):
        root = 'brands'
    else:
        root = 'defaults'

    extension = file_name.split('.')[-1]
    file_name = token_urlsafe(12)
    return f'{root}/{file_name}.{extension}'


class BaseModel(models.Model, URLKeyInterface):
    url_key = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def get_or_create(cls, name: str):
        name = name.title()
        url_key = cls.generate_url_key(name, validate_unique=False)

        try:
            instance = cls.objects.get(url_key=url_key)
        except ObjectDoesNotExist:
            instance = cls.objects.create(name=name, url_key=url_key)
        return instance

    def __str__(self):
        return self.name


class PageBanner(models.Model):
    page = models.CharField(max_length=20, choices=Pages.choices, unique=True)
    main_banner = models.ImageField(upload_to=upload_directory, blank=True)
    top_banner = models.ImageField(upload_to=upload_directory, blank=True)
    middle_right_banner = models.ImageField(upload_to=upload_directory, blank=True)
    bottom_left_banner = models.ImageField(upload_to=upload_directory, blank=True)
    bottom_right_banner = models.ImageField(upload_to=upload_directory, blank=True)
    image_vars = ['main_banner', 'top_banner', 'middle_right_banner', 'bottom_left_banner', 'bottom_right_banner']
    static_url = settings.STATIC_URL

    @classmethod
    def index_page(cls):
        return cls.objects.get(page=Pages.INDEX)

    def remove_image(self, image_name=None, image_var='image'):
        image = self.__getattribute__(image_var)
        image_name = image_name if image_name else image.name
        image.storage.delete(image_name)

    def get_banner_url(self, name):
        image = self.__getattribute__(name)
        if image:
            return image.url
        return ''

    def static_image(self, image_name):
        return self.static_url + 'img/' + image_name

    @property
    def main(self):
        return self.get_banner_url('main_banner') or self.static_image('banner_image.png')

    @property
    def top(self):
        return self.get_banner_url('top_banner') or self.static_image('middle_banner.png')

    @property
    def middle_right(self):
        return self.get_banner_url('middle_right_banner') or self.static_image('blue_bg.png')

    @property
    def bottom_left(self):
        return self.get_banner_url('bottom_left_banner') or self.static_image('skyblue_bg.png')

    @property
    def bottom_right(self):
        return self.get_banner_url('bottom_right_banner') or self.static_image('cross.png')

    def __str__(self):
        return self.page.capitalize() + ' Page Banners'


class Brand(BaseModel):
    logo = models.ImageField(upload_to=upload_directory, blank=True)


class Colour(BaseModel):
    url_key = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    hex = models.CharField(max_length=7, blank=True)


class Watch(BaseModel):

    class Meta:
        verbose_name_plural = 'watches'

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='watches', null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    device_type = models.CharField(max_length=150, default='Digital')
    gender = models.CharField(max_length=10, choices=Genders.choices, default=Genders.UNISEX)
    price = models.FloatField(default=0)
    currency = models.CharField(max_length=3, choices=Currencies.choices, default=Currencies.GBP)
    category = models.CharField(max_length=150, blank=True, null=True)
    hardware = models.CharField(max_length=150, blank=True, null=True)
    material = models.CharField(max_length=150, blank=True, null=True)
    diameter = models.CharField(max_length=150, blank=True, null=True)
    thickness = models.CharField(max_length=150, blank=True, null=True)
    colour = models.ForeignKey(Colour, on_delete=models.SET_NULL, related_name='watches', null=True)
    analogous_colours = models.CharField(max_length=150, blank=True, null=True)
    dial_colour = models.CharField(max_length=150, blank=True, null=True)
    strap_type = models.CharField(max_length=150, blank=True, null=True)
    strap_material = models.CharField(max_length=150, blank=True, null=True)
    strap_colour = models.CharField(max_length=150, blank=True, null=True)
    crystal_material = models.CharField(max_length=150, blank=True, null=True)
    stone_set = models.CharField(max_length=150, blank=True, null=True)
    case_shape = models.CharField(max_length=150, blank=True, null=True)
    water_resistance = models.CharField(max_length=150, blank=True, null=True)
    time = models.CharField(max_length=150, blank=True, null=True)
    calendar = models.CharField(max_length=150, blank=True, null=True)
    timers = models.CharField(max_length=150, blank=True, null=True)
    notifications = models.CharField(max_length=150, blank=True, null=True)
    fitness_tracker = models.CharField(max_length=150, blank=True, null=True)
    memory = models.CharField(max_length=150, blank=True, null=True)
    outdoor = models.CharField(max_length=150, blank=True, null=True)
    lighting = models.CharField(max_length=150, blank=True, null=True)
    movement_type = models.CharField(max_length=150, blank=True, null=True)
    movement_origin = models.CharField(max_length=150, blank=True, null=True)
    style = models.CharField(max_length=150, blank=True, null=True)
    display = models.CharField(max_length=150, blank=True, null=True)
    connectivity = models.CharField(max_length=150, blank=True, null=True)
    markers = models.CharField(max_length=150, blank=True, null=True)
    sports = models.CharField(max_length=150, blank=True, null=True)
    delivery = models.CharField(max_length=150, blank=True, null=True)
    warranty = models.CharField(max_length=150, blank=True, null=True)
    image_source = models.CharField(max_length=255, blank=True, null=True)
    source_link = models.CharField(max_length=255, blank=True, null=True)
    extra_fields = models.TextField()

    @classmethod
    def get_field_names(cls):
        return [field.name for field in cls._meta.fields if field.name not in ['id', 'url_key']]

    @classmethod
    def parse_brand(cls, name):
        if isinstance(name, str):
            return Brand.get_or_create(name)
        return None

    @classmethod
    def parse_colour(cls, name):
        if isinstance(name, str):
            return Colour.get_or_create(name)
        return None

    @classmethod
    def apply_filters(cls, filters: dict, search_text: str):
        brands = filters.get('brands')
        price_sort = filters.get('price_sort')
        min_price = filters.get('min_price')
        max_price = filters.get('max_price')
        colours = filters.get('colours')
        functions = filters.get('functions')
        deliveries = filters.get('deliveries')

        watches = cls.objects.filter()

        if search_text:
            watches = watches.filter(name__icontains=search_text) | \
                      watches.filter(brand__name__icontains=search_text) | \
                      watches.filter(colour__name__icontains=search_text) | \
                      watches.filter(strap_colour__icontains=search_text) | \
                      watches.filter(dial_colour__icontains=search_text)

        if brands:
            watches = watches.filter(brand__url_key__in=brands)
        if min_price:
            watches = watches.filter(price__gte=min_price)
        if max_price:
            watches = watches.filter(price__lte=max_price)
        if colours:
            watches = watches.filter(analogous_colours__in=colours)
        if deliveries:
            watches = watches.filter(delivery__in=deliveries)

        if price_sort == PriceSort.LOW_TO_HIGH:
            watches = watches.order_by('price')
        elif price_sort == PriceSort.HIGH_TO_LOW:
            watches = watches.order_by('-price')

        return watches

    @property
    def visible_fields(self):
        fields = [{
            'name': 'BRAND',
            'value': self.brand.name
        }]
        _fields = self.__dict__.copy()

        exclude_keys = [
            '_state', 'id', 'url_key', 'brand_id', 'extra_fields', 'source_link', 'image_source', 'created_at',
            'updated_at'
        ]
        _fields.update(self.get_extra_fields())

        for key in exclude_keys:
            del _fields[key]

        for name, value in _fields.items():
            if value:
                fields.append({
                    'name': name.replace('_', ' ').upper(),
                    'value': value
                })

        return fields

    @property
    def image_url(self):
        return self.image_source

    def get_extra_fields(self):
        return load_json(self.extra_fields.replace('\'', '"'))

    @property
    def price_fraction_seperated(self):
        return tuple(format(self.price, '.2f').split('.'))

    @property
    def price_integer(self):
        integer, _ = self.price_fraction_seperated
        return integer

    @property
    def price_fraction(self):
        _, fraction = self.price_fraction_seperated
        return fraction

    def __str__(self):
        return self.name
