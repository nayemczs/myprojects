from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from .models import Place, Region, Destination, Hotel, House, ApartmentType, Interest
from .forms import HotelFilterForm, HouseFilterForm, SearchForm
from magazine.utils import GoogleMaps, pagination_links


# Create your views here.
class BaseView(View):
    per_page = 12
    template_name = None
    context = None
    searched_city = None

    def get_page_number(self):
        page_number = self.request.GET.get('page', '1')
        page_number = page_number if page_number.isnumeric() else '1'
        return page_number

    def paginate(self, list_name, list_data):
        page_number = self.get_page_number()
        page = Paginator(list_data, per_page=self.per_page).page(page_number)
        if self.context is None:
            self.context = {}
        self.context.update({
            list_name: page.object_list,
            'page_number': page.number,
            'pagination_links': pagination_links(page, base_url=self.request.path)
        })

    def render(self):
        return render(self.request, self.template_name, self.context)

    def get_searched_city(self):
        search_form = SearchForm(self.request.POST or None, initial={'city': self.request.session.get('city', '')})
        if search_form.is_valid() and search_form.has_changed():
            self.request.session.update({'city': search_form.cleaned_data['city']})
        self.searched_city =  self.request.session.get('city')
        return self.searched_city


class BaseFilterView(BaseView):
    filter_form_class = None
    filter_session_name = None
    filter_form = None
    filters = None
    searched_city = None

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.filter_form = self.filter_form_class(request.POST or None)
        self.get_searched_city()
        self.get_filters()

    def get(self, request):
        return self.process()

    def post(self, request):
        return self.process()

    def process(self):
        return self.render()

    def get_filters(self):
        if self.filter_form.is_valid():
            self.request.session.update({self.filter_session_name: self.filter_form.cleaned_data})

        self.filters = self.request.session.get(self.filter_session_name, None)
        return self.filters


class ExploreView(BaseView):
    template_name = 'pages/explore_place.html'

    def get(self, request, place_id, landscape=None, interest=None):
        place = Place.get_or_fail(place_id)
        self.get_searched_city()

        destinations = place.get_destinations(landscape, interest, self.searched_city)
        self.context = {
            'place': place
        }
        self.paginate('destinations', destinations)
        self.context.update(place.destination_filter_options())
        return self.render()


class RegionsView(BaseView):
    template_name = 'pages/regions.html'

    def get(self, request, place_id, filter_key=None):
        place = Place.get_or_fail(place_id)

        self.context = {
            'place': place
        }
        self.paginate('regions', place.get_regions(land=filter_key))
        self.context.update(place.region_filter_options())
        return self.render()


class HotelListView(BaseFilterView):
    template_name = 'pages/hotel_listing.html'
    filter_form_class = HotelFilterForm
    filter_session_name = 'hotel_filters'

    def process(self):
        hotels = Hotel.apply_filters(self.filters, self.searched_city)
        self.paginate('hotels', hotels)
        self.context.update(Hotel.filter_options())
        return self.render()


class HouseRentListView(BaseFilterView):
    template_name = 'pages/house_rent_listing.html'
    filter_form_class = HouseFilterForm
    filter_session_name = 'house_filters'

    def process(self):
        houses = House.apply_filters(for_rent=True, filters=self.filters, city=self.searched_city)
        self.paginate('houses', houses)
        self.context.update(House.filter_options(for_rent=True))
        return self.render()


class HouseSaleListView(BaseFilterView):
    template_name = 'pages/house_sale_listing.html'
    filter_form_class = HouseFilterForm
    filter_session_name = 'house_filters'

    def process(self):
        houses = House.apply_filters(for_rent=False, filters=self.filters, city=self.searched_city)
        self.paginate('houses', houses)
        self.context.update(House.filter_options(for_rent=False))
        return self.render()


explore = ExploreView.as_view()
regions = RegionsView.as_view()
hotel_list = HotelListView.as_view()
house_rent_listing = HouseRentListView.as_view()
house_sale_listing = HouseSaleListView.as_view()


def index(request):
    # print(GoogleMaps.get_instance().get_geocode('1600 Amphitheatre Parkway, Mountain View, CA'))
    context = {
        'destinations': Destination.list_featured(),
        'houses_for_rent': House.list_featured().filter(for_rent=True),
        'houses_for_sale': House.list_featured().filter(for_rent=False),
        'hotels': Hotel.list_featured(),
        'apartment_types': ApartmentType.list_with_min_prices(),
        'interests': Interest.objects.all()
    }
    return render(request, 'pages/index.html', context)


def explore_region_or_destination(request, place_id, region_id=None, destination_id=None):
    context = None
    instance = None
    template = None

    if region_id:
        instance = Region.get_or_fail(
            url_key=region_id,
            place__url_key=place_id
        )
        context = {
            'region': instance
        }
        template = 'pages/explore_region.html'
    elif destination_id:
        instance = Destination.get_or_fail(
            url_key=destination_id,
            region__place__url_key=place_id
        )
        context = {
            'destination': instance
        }
        template = 'pages/explore_destination.html'

    context.update({
        'hotels': instance.hotels.all(),
        'houses_for_sale': instance.houses.filter(for_rent=False),
        'houses_for_rent': instance.houses.filter(for_rent=True)
    })
    return render(request, template, context)


def about_us(request):
    return render(request, 'pages/about_us.html')


def hotel_show(request, hotel_id):
    hotel = Hotel.get_or_fail(hotel_id)
    return render(request, 'pages/hotel_single_page.html', {'hotel': hotel})


def house_rent_single_page(request, house_id):
    house = House.get_or_fail(url_key=house_id, for_rent=True)
    context = {
        'house': house
    }
    return render(request, 'pages/house_rent_single_page.html', context)


def house_sale_single(request, house_id):
    house = House.get_or_fail(url_key=house_id, for_rent=False)
    context = {
        'house': house
    }
    return render(request, 'pages/house_sale_single.html', context)
