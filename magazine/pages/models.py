from django.conf.global_settings import LANGUAGES
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language
from magazine.exceptions import UrlKeyExistsException
from secrets import token_urlsafe
from re import sub as re_sub


# Create your models here.
def resource_directory_path(instance, file_name):
    extension = file_name.split('.')[-1]
    file_name = token_urlsafe(12)
    return f'resources/{file_name}.{extension}'


def generate_url_key():
    return token_urlsafe(5)


# Base and Abstract Classes
class BasicArticle(models.Model):
    name = models.CharField(max_length=255)
    article_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    article = models.TextField()

    class Meta:
        abstract = True


class TranslationInterface:
    is_translated = False
    translation = None

    def get_translation(self, name):
        self.translate()
        if self.translation:
            return getattr(self.translation, name)
        return getattr(self, name)

    def translate(self):
        if self.is_translated:
            return self.translation

        language_code = get_language()
        if language_code == 'en':
            self.translation = None
            self.is_translated = True
            return self.translation

        try:
            self.translation = self.translations.get(language=language_code)
        except ObjectDoesNotExist:
            self.translation = None
        self.is_translated = True
        return self.translation


class URLKeyInterface:
    url_key = None

    @classmethod
    def generate_url_key(cls, name=None):
        if name is None:
            name = cls.name

        key = re_sub(r'[\W_]+', '-', name.lower())
        key = re_sub('-$', '', key)
        try:
            cls.objects.get(url_key=key)
        except cls.DoesNotExist:
            pass
        else:
            raise UrlKeyExistsException(url_key=key)
        return key

    def search_key(self):
        return self.url_key


class Article(BasicArticle, TranslationInterface, URLKeyInterface):
    url_key = models.CharField(max_length=255, unique=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    is_featured = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to=resource_directory_path)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def get_or_fail(cls, search_key=None, **kwargs):
        if search_key:
            return get_object_or_404(cls, url_key=search_key)
        else:
            return get_object_or_404(cls, **kwargs)

    @classmethod
    def list_featured(cls):
        return cls.objects.filter(is_featured=True)

    def get_name(self):
        return self.get_translation('name')

    def get_article(self):
        return self.get_translation('article')

    def get_description(self):
        return self.get_translation('description')

    def get_location(self):
        return self.get_translation('location')

    def get_article_title(self):
        return self.get_translation('article_title')

    def get_image_gallery(self):
        return self.image_gallery.all()

    def image_url(self):
        return self.cover_image.url

    def delete(self, using=None, keep_parents=False):
        self.remove_image()
        return super().delete(using=using, keep_parents=keep_parents)

    def remove_image(self):
        print('deleting image:', self.cover_image.name)
        self.cover_image.storage.delete(self.cover_image.name)

    def __str__(self):
        return self.name


class Apartment(Article):
    price = models.IntegerField(default=0, verbose_name='price in euros')
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    living_area = models.IntegerField(default=0, verbose_name='living area in metres squared')
    garden = models.IntegerField(default=0, verbose_name='garden area in metres squared')
    land = models.IntegerField(default=0, verbose_name='land area in metres squared')
    guests = models.IntegerField(default=0)
    contact_address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=12)
    contact_email = models.EmailField(max_length=255)
    website_link = models.URLField(max_length=255, blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    instagram_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)
    google_link = models.URLField(max_length=255, blank=True)

    class Meta:
        abstract = True

    @classmethod
    def _apply_filters(cls, filters=None, city=None):
        instances = cls.objects.filter()

        if filters is None:
            return instances

        regions = filters.get('regions')
        facilities = filters.get('facilities')

        if city:
            instances = instances.filter(city__name__icontains=city)
        if regions:
            instances = instances.filter(city__region__url_key__in=regions)
        if facilities:
            instances = instances.filter(facilities__in=facilities)

        return instances

    def get_price(self):
        return self.get_translation('price')

    def get_bedrooms(self):
        return self.get_translation('bedrooms')

    def get_bathrooms(self):
        return self.get_translation('bathrooms')

    def get_living_area(self):
        return self.get_translation('living_area')

    def get_garden(self):
        return self.get_translation('garden')

    def get_land(self):
        return self.get_translation('land')

    def get_guests(self):
        return self.get_translation('guests')

    def get_contact_address(self):
        return self.get_translation('contact_address')

    def get_contact_number(self):
        return self.get_translation('contact_number')

    def get_room_images(self):
        return self.room_images.all()

    def get_featured_images(self):
        return self.featured_images.all()

    def get_image_gallery(self):
        images = []
        images.extend(self.get_room_images())
        images.extend(self.get_featured_images())
        return images

    def get_facilities(self):
        return self.facilities.all()

    def get_type(self):
        return self.type.get_name()


class Category(models.Model, TranslationInterface):
    name = models.CharField(max_length=255)

    def get_name(self):
        return self.get_translation('name')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Translation(BasicArticle):
    language = models.CharField(max_length=7, choices=LANGUAGES, unique=True)
    default = None

    def __str__(self):
        return self.language

    class Meta:
        abstract = True


class ApartmentTranslation(Translation):
    price = models.CharField(max_length=25, default='0')
    bedrooms = models.CharField(max_length=25, default='0')
    bathrooms = models.CharField(max_length=25, default='0')
    living_area = models.CharField(max_length=25, default='0', verbose_name='living area in metres squared')
    garden = models.CharField(max_length=25, default='0', verbose_name='garden area in metres squared')
    land = models.CharField(max_length=25, default='0', verbose_name='land area in metres squared')
    guests = models.CharField(max_length=25, default='0')
    contact_address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=12)

    class Meta:
        abstract = True


class CategoryTranslation(models.Model):
    language = models.CharField(max_length=7, choices=LANGUAGES, unique=True)
    name = models.CharField(max_length=255)
    default = None

    class Meta:
        abstract = True


# Models
class Place(Article):

    @classmethod
    def destination_filter_options(cls):
        return {
            'landscapes': Landscape.objects.all(),
            'interests': Interest.objects.all()
        }

    def region_filter_options(self):
        return {
            'lands': self.lands.all()
        }

    def get_destinations(self, landscape_filter=None, interest_filter=None, city=None):
        return Destination.apply_filters(self, landscape_filter, interest_filter, city)

    def get_regions(self, land=None):
        return Region.apply_filters(self, land)


class PlaceTranslation(Translation):
    default = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='translations')


class Region(Article):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='regions')
    land = models.ForeignKey('pages.Land', on_delete=models.CASCADE, related_name='regions')

    @classmethod
    def apply_filters(cls, place=None, land=None):
        regions = cls.objects.filter()

        if place:
            regions = regions.filter(place=place)
        if land:
            pass

        return regions

    @property
    def hotels(self):
        return Hotel.objects.filter(city__region=self)

    @property
    def houses(self):
        return House.objects.filter(city__region=self)


class RegionTranslation(Translation):
    default = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='translations')
    
    
class Destination(Article):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='destinations')
    landscapes = models.ManyToManyField('pages.Landscape', related_name='destinations', blank=True)
    interests = models.ManyToManyField('pages.Interest', related_name='destinations', blank=True)

    @classmethod
    def apply_filters(cls, place=None, landscape_filter=None, interest_filter=None, city=None):
        destinations = cls.objects.filter()

        if place:
            destinations = destinations.filter(region__place=place)
        if city:
            destinations = destinations.filter(name__icontains=city)
        if landscape_filter:
            destinations = destinations.filter(landscapes__url_key=landscape_filter)
        if interest_filter:
            destinations = destinations.filter(interests__url_key=interest_filter)

        return destinations

    def get_landscapes(self):
        return self.landscapes.all()


class DestinationTranslation(Translation):
    default = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='translations')


class Hotel(Apartment):
    city = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='hotels')
    type = models.ForeignKey('pages.HotelType', on_delete=models.CASCADE, related_name='hotels')
    facilities = models.ManyToManyField('pages.Facility', related_name='hotels', blank=True)

    @classmethod
    def apply_filters(cls, filters=None, city=None):
        hotels = super()._apply_filters(filters, city)

        if filters is None:
            return hotels

        hotel_types = filters.get('hotel_types')

        if hotel_types:
            hotels = hotels.filter(type__in=hotel_types)

        return hotels

    @classmethod
    def filter_options(cls):
        return {
            'hotel_types': HotelType.objects.all(),
            'facilities': Facility.objects.all(),
            'regions': Region.objects.all()
        }


class HotelTranslation(ApartmentTranslation):
    default = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='translations')


class House(Apartment):
    url_key = models.CharField(max_length=32, default=generate_url_key, unique=True)
    city = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='houses')
    type = models.ForeignKey('pages.ApartmentType', on_delete=models.CASCADE, related_name='houses')
    condition = models.ForeignKey(
        'pages.ApartmentCondition',
        on_delete=models.CASCADE,
        related_name='houses',
        blank=True,
        null=True
    )
    for_rent = models.BooleanField(default=False)
    facilities = models.ManyToManyField('pages.Facility', related_name='houses', blank=True)

    @classmethod
    def apply_filters(cls, for_rent, filters=None, city=None):
        houses = super()._apply_filters(filters, city)
        houses = houses.filter(for_rent=for_rent)

        if filters is None:
            return houses

        house_types = filters.get('house_types')
        conditions = filters.get('conditions')

        if house_types:
            houses = houses.filter(type__in=house_types)
        if not for_rent and conditions:
            houses = houses.filter(condition__in=conditions)

        return houses

    @classmethod
    def filter_options(cls, for_rent=False):
        filters = {
            'house_types': ApartmentType.list_with_house_counts(for_rent),
            'facilities': Facility.objects.all(),
            'regions': Region.objects.all()
        }
        if not for_rent:
            filters.update({'conditions': ApartmentCondition.objects.all()})
        return filters

    def get_condition(self):
        return self.condition.get_name()

    def thumbnail(self):
        return self.featured_images.first().image_url()


class HouseTranslation(ApartmentTranslation):
    default = models.ForeignKey(House, on_delete=models.CASCADE, related_name='translations')


class Land(Category, URLKeyInterface):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='lands')
    url_key = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.place.__str__()}: {self.name}'


class LandTranslation(CategoryTranslation):
    default = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='translations')


class Facility(Category):
    pass


class FacilityTranslation(CategoryTranslation):
    default = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='translations')


class HotelType(Category):
    pass


class HotelTypeTranslation(CategoryTranslation):
    default = models.ForeignKey(HotelType, on_delete=models.CASCADE, related_name='translations')


class ApartmentType(Category):
    pass

    @classmethod
    def list_with_house_counts(cls, for_rent=False):
        house_count = models.Count('houses', filter=models.Q(houses__for_rent=for_rent))
        return cls.objects.annotate(house_count=house_count)

    @classmethod
    def list_with_min_prices(cls, for_rent=False):
        starting_price = models.Min('houses__price', filter=models.Q(houses__for_rent=for_rent))
        return cls.objects.annotate(starting_price=starting_price)


class ApartmentTypeTranslation(CategoryTranslation):
    default = models.ForeignKey(ApartmentType, on_delete=models.CASCADE, related_name='translations')


class ApartmentCondition(Category):
    pass


class ApartmentConditionTranslation(CategoryTranslation):
    default = models.ForeignKey(ApartmentCondition, on_delete=models.CASCADE, related_name='translations')


class Landscape(Category, URLKeyInterface):
    url_key = models.CharField(max_length=255, unique=True)


class LandscapeTranslation(CategoryTranslation):
    default = models.ForeignKey(Landscape, on_delete=models.CASCADE, related_name='translations')


class Interest(Category, URLKeyInterface):
    url_key = models.CharField(max_length=255, unique=True)


class InterestTranslation(CategoryTranslation):
    default = models.ForeignKey(Interest, on_delete=models.CASCADE, related_name='translations')


class Resource(models.Model):
    item = models.ImageField(upload_to=resource_directory_path)

    class Meta:
        abstract = True

    @classmethod
    def save_file(cls, file):
        resource = cls.objects.create(item=file)
        resource.save()
        return resource.image_url()

    def delete(self, using=None, keep_parents=False):
        self.item.storage.delete(self.item.name)
        return super().delete(using=using, keep_parents=keep_parents)

    def remove_image(self):
        self.item.storage.delete(self.item.name)

    def image_url(self):
        return self.item.url

    def __str__(self):
        return self.item.url


class ApartmentResource(Resource):
    featured_by_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='featured_images', null=True)
    rooms_of_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_images', null=True)
    featured_by_house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='featured_images', null=True)
    rooms_of_house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='room_images', null=True)


class ImageGallery(Resource):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='image_gallery', null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='image_gallery', null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='image_gallery', null=True)
