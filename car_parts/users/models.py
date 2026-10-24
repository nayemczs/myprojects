from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.utils.timezone import now as current_time
from django.utils.translation import gettext_lazy as _
from secrets import token_urlsafe
from p_shope.exceptions import InsufficientQuantityException


def user_directory_path(instance, file_name):
    extension = file_name.split('.')[-1]
    file_name = token_urlsafe(12)
    return f'uploads/{instance.user.username}/{file_name}.{extension}'


# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(
        error_messages={'unique': _('A user with that username already exists.')},
        help_text=_('Required. 10 characters or fewer.'),
        max_length=254,
        unique=True,
        primary_key=True,
        validators=[UnicodeUsernameValidator(), MinLengthValidator(3)],
        verbose_name=_('username')
    )
    email = models.CharField(
        error_messages={'unique': _('This email address has already been registered.')},
        max_length=254,
        unique=True,
        verbose_name=_('email address')
    )
    is_vendor = models.BooleanField(default=False)

    def create_user_profile(self, first_name, last_name, address, image):
        Profile.objects.create(
            user=self,
            first_name=first_name,
            last_name=last_name,
            address=address,
            image=image
        )

    def create_vendor_profile(self, name, region, country, city, address, image):
        VendorProfile.objects.create(
            user=self,
            name=name,
            region=region,
            country=country,
            city=city,
            address=address,
            image=image
        )

    def full_name(self):
        if self.is_vendor:
            return self.vendor_profile.name
        return f'{self.profile.first_name} {self.profile.last_name}'

    def __str__(self):
        return f'{self.username}'

    def delete(self, using=None, keep_parents=False):
        try:
            self.profile.delete()
            self.vendor_profile.delete()
        except ObjectDoesNotExist:
            pass
        super().delete(using=using, keep_parents=keep_parents)


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_('first name'))
    last_name = models.CharField(max_length=150, verbose_name=_('last name'))
    address = models.CharField(max_length=245, verbose_name=_('address'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    image = models.ImageField(upload_to=user_directory_path)

    def get_cart(self, session_id):
        try:
            cart = self.cart
        except ObjectDoesNotExist:
            cart = Cart.objects.create(
                session_id=session_id,
                profile=self,
                total=0
            )
        else:
            if cart.session_id != session_id:
                cart.delete()
                cart = Cart.objects.create(
                    session_id=session_id,
                    profile=self,
                    total=0
                )

        return cart

    def add_to_cart(self, session_id, product, quantity):
        cart = self.get_cart(session_id)
        cart.add_product(product, quantity)

    def update_cart(self, session_id, product, quantity):
        cart = self.get_cart(session_id)
        cart.update_product(product, quantity)

    def remove_from_cart(self, session_id, product_id):
        cart = self.get_cart(session_id)
        cart.remove_product(product_id)

    def clear_cart(self, session_id):
        cart = self.get_cart(session_id)
        for product_id in cart.products.values_list('id', flat=True):
            cart.remove_product(product_id)

    def remove_cart(self):
        try:
            self.cart.delete()
        except ObjectDoesNotExist:
            pass

    def place_order(self, session_id):
        cart_items = self.get_cart(session_id).cart_items.all()
        if not cart_items:
            raise PermissionDenied(_('Cart has no items'))

        order = self.orders.create(
            session_id=self.cart.session_id,
            profile=self,
            total=self.cart.total
        )
        for cart_item in cart_items:
            order.products.add(
                cart_item.product,
                through_defaults={'quantity': cart_item.quantity, 'sub_total': cart_item.sub_total}
            )
            self.cart.products.remove(cart_item.product)

    def order_info(self):
        completed_orders = []
        pending_orders = []

        for order in self.orders.filter(order_items__is_completed=True).distinct():
            for item in order.order_items.all():
                completed_orders.append(item)
        for order in self.orders.filter(order_items__is_completed=False).distinct():
            for item in order.order_items.all():
                pending_orders.append(item)
        return {'completed_orders': completed_orders, 'pending_orders': pending_orders}

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def image_url(self):
        return self.image.url

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete(using=using, keep_parents=keep_parents)


class VendorProfile(models.Model):
    name = models.CharField(max_length=245, verbose_name=_('company name'))
    region = models.CharField(max_length=245, verbose_name=_('region'))
    country = models.CharField(max_length=245, verbose_name=_('country'))
    city = models.CharField(max_length=245, verbose_name=_('city'))
    address = models.CharField(max_length=245, verbose_name=_('address'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='vendor_profile')
    image = models.ImageField(upload_to=user_directory_path)

    def add_product(self, product, images):
        product.save_with_images(self, images)

    def update_product(self, product, updated_product):
        if product.vendor.user_id != self.user_id:
            raise PermissionDenied(_('Product does NOT exist'))

        product.model_name = updated_product.model_name
        product.part_name = updated_product.part_name
        product.description = updated_product.description
        product.price = updated_product.price
        product.quantity = updated_product.quantity
        product.save()

    def remove_product(self, product_id):
        pass

    def add_product_image(self, product_id, image):
        try:
            product = self.products.get(id=product_id)
            product.images.create(image=image)
        except ObjectDoesNotExist:
            raise PermissionDenied(_('Image does NOT exist'))

    def update_product_image(self, product_id, image_id, image):
        try:
            product = self.products.get(id=product_id)
            product.update_image(image_id, image)
        except ObjectDoesNotExist:
            raise PermissionDenied(_('Image does NOT exist'))

    def remove_product_image(self, product_id, image_id):
        try:
            product = self.products.get(id=product_id)
            product.remove_image(image_id)
        except ObjectDoesNotExist:
            raise PermissionDenied(_('Image does NOT exist'))

    def order_info(self):
        completed_orders = []
        pending_orders = []

        for item in OrderItem.objects.filter(product__vendor=self, is_completed=True):
            completed_orders.append(item)
        for item in OrderItem.objects.filter(product__vendor=self, is_completed=False):
            pending_orders.append(item)
        return {'completed_orders': completed_orders, 'pending_orders': pending_orders}

    def mark_order(self, product_id, item_id):
        try:
            product = self.products.get(id=product_id, order_info__id=item_id)
            order_info = product.order_info.get(id=item_id)
            order_info.is_completed = not order_info.is_completed
            order_info.date_confirmed = current_time()
            order_info.save()
        except ObjectDoesNotExist:
            raise PermissionDenied(_('Product does NOT exist'))

    def __str__(self):
        return f'{self.name}'

    def image_url(self):
        return self.image.url

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete(using=using, keep_parents=keep_parents)


class Cart(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, unique=True, related_name='cart')
    products = models.ManyToManyField('products.Product', through='CartItem', related_name='carts')
    total = models.FloatField()

    def add_product(self, product, quantity):
        if product.quantity < quantity:
            raise InsufficientQuantityException()

        try:
            self.cart_items.get(product=product)
        except ObjectDoesNotExist:
            product.quantity -= quantity
            self.products.add(product, through_defaults={'quantity': quantity, 'sub_total': quantity * product.price})
            product.save()
            self.total += quantity * product.price
            self.save()
        else:
            self.update_product(product, quantity)

    def update_product(self, product, quantity):
        cart_item = self.cart_items.get(product=product)
        product.quantity += cart_item.quantity

        if product.quantity < quantity:
            raise InsufficientQuantityException()

        product.quantity -= quantity
        cart_item.quantity = quantity
        self.total -= cart_item.sub_total
        cart_item.sub_total = quantity * product.price
        self.total += cart_item.sub_total
        product.save()
        cart_item.save()
        self.save()

    def remove_product(self, product_id):
        try:
            cart_item = self.cart_items.get(product__id=product_id)
        except ObjectDoesNotExist:
            pass
        else:
            self.total -= cart_item.sub_total
            cart_item.product.quantity += cart_item.quantity
            cart_item.product.save()
            self.products.remove(cart_item.product)
            self.save()

    def delete(self, using=None, keep_parents=False):
        for product_id in self.products.values_list('id', flat=True):
            self.remove_product(product_id)
        super().delete(using=using, keep_parents=keep_parents)

    def __str__(self):
        return f'{self.profile.user.username}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='cart_info')
    quantity = models.IntegerField()
    sub_total = models.FloatField()


class Order(models.Model):
    session_id = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField('products.Product', through='OrderItem', related_name='orders')
    total = models.FloatField()
    date_purchased = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.profile.user.username} {self.date_purchased}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_info')
    quantity = models.IntegerField()
    sub_total = models.FloatField()
    is_completed = models.BooleanField(default=False)
    date_confirmed = models.DateTimeField(null=True)
