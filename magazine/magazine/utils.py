from django.conf import settings
from .exceptions import LocationNotFoundException
from googlemaps import Client
from json import loads as json_loads


class GoogleMaps:
    __can_get_instance = False
    __instance = None

    def __init__(self):
        if not GoogleMaps.__can_get_instance:
            raise Exception("Illegal Usage. Please use the get_instance to obtain an instance.")

        self.__client = Client(key=settings.GOOGLE_API_KEY)

    @classmethod
    def get_instance(cls):
        """
        Get Google Maps instance through this class method.

        :return: Google Maps instance.
        """
        if GoogleMaps.__instance is None:
            GoogleMaps.__can_get_instance = True
            GoogleMaps.__instance = GoogleMaps()
            GoogleMaps.__can_get_instance = False
        return GoogleMaps.__instance

    def get_geocode(self, address):
        response = self.__client.geocode(address)

        try:
            location = response[0]['geometry']['location']
            return location['lat'], location['lng']
        except IndexError:
            raise LocationNotFoundException()


def pagination_links(page, base_url):
    base_url = base_url + '?page='
    links = []
    page_range = page.paginator.page_range

    if page.has_previous():
        previous_page = page.previous_page_number()
        if previous_page > page_range[0]:
            links.append({'text': page_range[0], 'class': 'prev', 'url': base_url + str(page_range[0])})
        if previous_page > page_range[1]:
            links.append({'text': '...', 'class': 'blank', 'url': '#'})
        links.append({'text': previous_page, 'class': 'prev', 'url': base_url + str(previous_page)})

    links.append({'text': page.number, 'class': 'active', 'url': base_url + str(page.number)})

    if page.has_next():
        next_page = page.next_page_number()
        links.append({'text': next_page, 'class': 'next', 'url': base_url + str(next_page)})
        if next_page < page_range[-2]:
            links.append({'text': '...', 'class': 'blank', 'url': '#'})
        if next_page < page_range[-1]:
            links.append({'text': page_range[-1], 'class': '', 'url': base_url + str(page_range[-1])})
    return links
