from django.contrib import admin
from .models import Customer, Item, Courier, FedEx, Shipment, Waybill

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Courier)
admin.site.register(FedEx)
admin.site.register(Shipment)
admin.site.register(Waybill)

