from rest_framework import serializers
from .models import Member, Order, Track


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('order_id', 'created_date',
                  'shipping_date', 'mobile_no', 'pickup_address', 'dropoff_address')
        model = Order


class MemberSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        fields = ('mob_no', 'real_name', 'tz', 'orders',)
        model = Member


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('order_id', 'request', 'request_time', 'accepted', 'accepted_time',
                  'arrived', 'arrived_time', 'delivered', 'delivered_time', )
        model = Track
