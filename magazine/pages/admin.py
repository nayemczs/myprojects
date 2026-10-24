from django.contrib.admin import site, register, ModelAdmin, StackedInline, TabularInline
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ngettext
from .models import (
    Place, Land, Region, Destination, House, Hotel, ApartmentResource, ImageGallery,
    Facility,  HotelType, ApartmentType, ApartmentCondition, Landscape, Interest,
    PlaceTranslation, DestinationTranslation, LandTranslation, RegionTranslation, HotelTranslation, HouseTranslation,
    FacilityTranslation, HotelTypeTranslation, ApartmentTypeTranslation, ApartmentConditionTranslation,
    LandscapeTranslation, InterestTranslation
)
from .forms import (
    PlaceForm, RegionForm, DestinationForm, HotelForm, HouseForm, LandscapeForm, InterestForm, LandForm
)


# Register your models here.
site.site_header = 'Magazine Admin Area'
site.site_title = 'Magazine Admin Area'
site.site_index = 'Magazine to No Knot Club Admin Area'


# Base Admin Class
class BaseAdmin(ModelAdmin):

    def delete_queryset(self, request, queryset):
        for item in queryset:
            item.delete()


class URLKeyAdminInterface:
    readonly_fields = ['url_key']

    def save_model(self, request, obj, form, change):
        url_key = form.cleaned_data.get('url_key')
        if url_key:
            obj.url_key = url_key
        return super().save_model(request, obj, form, change)


class ArticleAdmin(BaseAdmin):
    list_display = ['__str__', 'is_featured']
    readonly_fields = ['lat', 'lng', 'url_key']
    actions = ['mark_featured', 'unmark_featured']

    def save_model(self, request, obj, form, change):
        url_key = form.cleaned_data.get('url_key')
        if url_key:
            obj.url_key = url_key

        if change and 'cover_image' in form.changed_data:
            previous = self.model.objects.get(id=obj.id)
            previous.remove_image()
        return super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        for form in formset:
            if change and 'item' in form.changed_data:
                instance = form.instance
                try:
                    previous = instance.__class__.objects.get(id=instance.id)
                    previous.remove_image()
                except ObjectDoesNotExist:
                    pass
        super().save_formset(request, form, formset, change)

    def mark_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, ngettext(
            '%d Article was successfully marked as featured.',
            '%d Articles were successfully marked as featured.',
            updated,
        ) % updated, messages.SUCCESS)
    mark_featured.short_description = 'Mark selected Articles as Featured'

    def unmark_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, ngettext(
            '%d Article was successfully unmarked as featured.',
            '%d Articles were successfully unmarked as featured.',
            updated,
        ) % updated, messages.SUCCESS)
    unmark_featured.short_description = 'Unmark selected Articles as Featured'


class CategoryAdmin(ModelAdmin):
    pass


class ResourceAdmin(BaseAdmin):
    exclude = []

    def has_module_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        if change and 'item' in form.changed_data:
            previous = self.model.objects.get(id=obj.id)
            previous.remove_image()
        return super(BaseAdmin, self).save_model(request, obj, form, change)


# Translation Inline Classes
class TranslationInline(StackedInline):
    extra = 1


class PlaceTranslationInline(TranslationInline):
    model = PlaceTranslation


class LandTranslationInline(TranslationInline):
    model = LandTranslation


class RegionTranslationInline(TranslationInline):
    model = RegionTranslation


class DestinationTranslationInline(TranslationInline):
    model = DestinationTranslation


class HouseTranslationInline(TranslationInline):
    model = HouseTranslation


class HotelTranslationInline(TranslationInline):
    model = HotelTranslation


class FacilityTranslationInline(TranslationInline):
    model = FacilityTranslation


class HotelTypeTranslationInline(TranslationInline):
    model = HotelTypeTranslation


class ApartmentTypeTranslationInline(TranslationInline):
    model = ApartmentTypeTranslation


class ApartmentConditionTranslationInline(TranslationInline):
    model = ApartmentConditionTranslation


class LandscapeTranslationInline(TranslationInline):
    model = LandscapeTranslation


class InterestTranslationInline(TranslationInline):
    model = InterestTranslation


# Image Gallery Inline Classes
class ImageGalleryInline(TabularInline):
    verbose_name = 'Image'
    verbose_name_plural = 'Image Gallery'
    model = ImageGallery
    extra = 1


class PlaceImageGalleryInline(ImageGalleryInline):
    fk_name = 'place'
    exclude = ['region', 'destination']


class RegionImageGalleryInline(ImageGalleryInline):
    fk_name = 'region'
    exclude = ['place', 'destination']


class DestinationImageGalleryInline(ImageGalleryInline):
    fk_name = 'destination'
    exclude = ['place', 'region']


class HotelFeaturedImagesInline(TabularInline):
    verbose_name = 'Featured Image'
    verbose_name_plural = 'Featured Images'
    model = ApartmentResource
    extra = 1
    fk_name = 'featured_by_hotel'
    exclude = ['featured_by_house', 'rooms_of_house', 'rooms_of_hotel']


class HotelRoomsImagesInline(TabularInline):
    verbose_name = 'Room Image'
    verbose_name_plural = 'Room Images'
    model = ApartmentResource
    extra = 1
    fk_name = 'rooms_of_hotel'
    exclude = ['featured_by_hotel',  'featured_by_house', 'rooms_of_house']


class HouseFeaturedImagesInline(TabularInline):
    verbose_name = 'Featured Image'
    verbose_name_plural = 'Featured Images'
    model = ApartmentResource
    extra = 1
    fk_name = 'featured_by_house'
    exclude = ['featured_by_hotel', 'rooms_of_house', 'rooms_of_hotel']


class HouseRoomsImagesInline(TabularInline):
    verbose_name = 'Room Image'
    verbose_name_plural = 'Room Images'
    model = ApartmentResource
    extra = 1
    fk_name = 'rooms_of_house'
    exclude = ['featured_by_hotel', 'featured_by_house', 'rooms_of_hotel']


# Admin Entries
@register(Place)
class PlaceAdmin(ArticleAdmin):
    inlines = [PlaceImageGalleryInline, PlaceTranslationInline]
    form = PlaceForm


@register(Region)
class RegionAdmin(ArticleAdmin):
    inlines = [RegionImageGalleryInline, RegionTranslationInline]
    form = RegionForm


@register(Destination)
class DestinationAdmin(ArticleAdmin):
    inlines = [DestinationImageGalleryInline, DestinationTranslationInline]
    form = DestinationForm


@register(Hotel)
class HotelAdmin(ArticleAdmin):
    inlines = [HotelFeaturedImagesInline, HotelRoomsImagesInline, HotelTranslationInline]
    form = HotelForm


@register(House)
class HouseAdmin(ArticleAdmin):
    list_display = ['__str__', 'for_rent', 'is_featured']
    inlines = [HouseFeaturedImagesInline, HouseRoomsImagesInline, HouseTranslationInline]
    form = HouseForm


@register(Land)
class LandAdmin(URLKeyAdminInterface, CategoryAdmin):
    inlines = [LandTranslationInline]
    form = LandForm


@register(Facility)
class FacilityAdmin(CategoryAdmin):
    inlines = [FacilityTranslationInline]


@register(HotelType)
class HotelTypeAdmin(CategoryAdmin):
    inlines = [HotelTypeTranslationInline]


@register(ApartmentType)
class ApartmentTypeAdmin(CategoryAdmin):
    inlines = [ApartmentTypeTranslationInline]


@register(ApartmentCondition)
class ApartmentConditionAdmin(CategoryAdmin):
    inlines = [ApartmentConditionTranslationInline]


@register(Landscape)
class LandscapeAdmin(URLKeyAdminInterface, CategoryAdmin):
    inlines = [LandscapeTranslationInline]
    form = LandscapeForm


@register(Interest)
class InterestAdmin(URLKeyAdminInterface, CategoryAdmin):
    inlines = [InterestTranslationInline]
    form = InterestForm


@register(ApartmentResource)
class ApartmentResourceAdmin(ResourceAdmin):
    pass


@register(ImageGallery)
class ImageGalleryAdmin(ResourceAdmin):
    pass
