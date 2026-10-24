from django.db import models
from django.utils.translation import gettext_lazy as _
from secrets import token_urlsafe


def user_directory_path(instance, file_name):
    extension = file_name.split('.')[-1]
    file_name = token_urlsafe(12)
    return f'uploads/{instance.product.vendor.user.username}/{file_name}.{extension}'


# Create your models here.
class Product(models.Model):
    model_name = models.CharField(max_length=245, verbose_name=_('model name'))
    part_name = models.CharField(max_length=245, verbose_name=_('part name'))
    description = models.CharField(max_length=245, verbose_name=_('description'))
    price = models.FloatField(verbose_name=_('price'))
    quantity = models.IntegerField(verbose_name=_('quantity'))
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    vendor = models.ForeignKey('users.VendorProfile', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.part_name}, {self.model_name}'

    @classmethod
    def apply_filters(cls, part_names, model_names, area):
        products = cls.objects.filter(
            model_name__in=model_names,
            part_name__in=part_names
        )

        area = area.split('_')
        if area[0] == 'region':
            products = products.filter(vendor__region__contains=area[1])
        elif area[0] == 'country':
            products = products.filter(vendor__country__contains=area[1])
        elif area[0] == 'city':
            products = products.filter(vendor__city__contains=area[1])
        return products

    def save_with_images(self, vendor, images):
        self.vendor = vendor
        self.save()
        self.add_images(images)

    def add_images(self, images):
        for image in images:
            self.images.create(image=image)

    def update_image(self, image_id, new_image):
        image = self.images.get(id=image_id)
        image.delete()
        self.images.create(image=new_image)

    def remove_image(self, image_id):
        image = self.images.get(id=image_id)
        image.delete()


class Resource(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=user_directory_path)

    def image_url(self):
        return self.image.url

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete(using=using, keep_parents=keep_parents)
