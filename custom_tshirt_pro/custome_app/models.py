from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    gen = [('Male', 'Male'), ('Female', 'Female')]
    customer_name = models.CharField(max_length=50)
    customer_mobile_no = models.IntegerField()
    gender = models.CharField(max_length=50, choices=gen)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')

    def __str__(self):
        return f'{self.customer_name}'


class Owner(models.Model):
    gen = [('Male', 'Male'), ('Female', 'Female')]
    owner_name = models.CharField(max_length=50)
    owner_percentage_share = models.FloatField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.owner_name}'


class Address(models.Model):
    land_mark = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='India')
    pin = models.CharField(max_length=6)
    longitude = models.FloatField(null=True, blank=True)
    lattitude = models.FloatField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    default_address = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class ItemType(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, blank=False, null=False)
    start_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    discount_percentage = models.FloatField(default=0)
    minimum_amount = models.FloatField(default=0)

    def __str__(self):
        return f'{self.code}'


class ItemSize(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


def upload_to(instance, filename):
    return f'{instance.id}/{filename}'


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f'{self.category} {self.name}'


class Font(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    name = models.CharField(max_length=200)
    item_size = models.ForeignKey(ItemSize, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    price = models.FloatField()
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name='items')

    class Meta:
        unique_together = ('name', 'subcategory')


class OrderMaster(models.Model):
    placed_on = models.DateTimeField()
    order_no = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    total_amount = models.FloatField(default=0)
    discount_percentage = models.FloatField(default=0)
    shipment_charges = models.FloatField(default=0)
    final_amount = models.FloatField(default=0)  # total_amount - discount + shipment_charges
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')


class OrderedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordered_items')
    order_master = models.ForeignKey(OrderMaster, on_delete=models.CASCADE, related_name='ordered_items')
    quantity = models.IntegerField()
    font = models.ForeignKey(Font, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to=upload_to, null=True, blank=True)
    custom_text = models.CharField(max_length=200, null=True, blank=True)
    unit_price = models.FloatField()
    total_amount = models.FloatField(default=0)





