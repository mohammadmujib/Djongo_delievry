from django.db import models
from phone_field import PhoneField


class Member(models.Model):
    mob_no = PhoneField(primary_key=True, help_text='Contact phone number')
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)


class Order(models.Model):
    member = models.ForeignKey(
        Member, related_name='orders', null=True, on_delete=models.SET_NULL)
    order_id = models.AutoField(primary_key=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateField(auto_now=False, blank=True, null=True)
    mobile_no = PhoneField(blank=True, help_text='Contact phone number')
    pickup_address = models.CharField(max_length=150)
    dropoff_address = models.CharField(max_length=150)


class Track(models.Model):
    order_id = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    request = models.BooleanField(default=True)
    request_time = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField()
    accepted_time = models.DateTimeField(auto_now=False, null=True, blank=True)
    arrived = models.BooleanField()
    arrived_time = models.DateTimeField(auto_now=False, null=True, blank=True)
    delivered = models.BooleanField()
    delivered_time = models.DateTimeField(
        auto_now=False, null=True, blank=True)
