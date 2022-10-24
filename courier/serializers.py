from rest_framework import serializers

from .models import Courier
from .models import Customer
from .models import Item
from .models import FedEx
from .models import Shipment
from .models import Waybill


class CourierSerializer(serializers.ModelSerializer):
   class Meta:
        model = Courier
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
   class Meta:
        model = Item
        fields = '__all__'


class FedExSerializer(serializers.ModelSerializer):
    class Meta:
        model = FedEx
        fields = '__all__'



class ShipmentSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.name')
    item = serializers.ReadOnlyField(source='item.name')
    courier = serializers.ReadOnlyField(source='courier.name')
    class Meta:
        model = Shipment
        fields = '__all__'


class WaybillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waybill
        fields = '__all__'
