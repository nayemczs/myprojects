from django.core.management.base import BaseCommand
from ...models import PageBanner
from thilter.utils import Pages


class Command(BaseCommand):
    help = 'Create PageBanner instance for Index Page.'

    def handle(self, *args, **options):
        PageBanner.objects.create(page=Pages.INDEX)
        self.stdout.write(self.style.SUCCESS('Banners Created.'))
