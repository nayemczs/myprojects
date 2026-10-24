from django.db.models import TextChoices, IntegerChoices


class Currencies(TextChoices):
    GBP = 'GBP'
    USD = 'USD'
    EUR = 'EUR'


class Genders(TextChoices):
    MALE = 'male'
    FEMALE = 'female'
    UNISEX = 'unisex'


class PriceSort(TextChoices):
    LOW_TO_HIGH = 0
    HIGH_TO_LOW = 1


class Pages(TextChoices):
    INDEX = 'index'
