from django.urls import path

from . import views

urlpatterns = [
    path('waybill', views.createWaybill, name='createWaybill'),
    path('label/waybill/<int:id>', views.WaybillLabel, name='WaybillLabel'),
    path('status/shipment/<int:id>', views.shipmentStatus, name='shipmentStatus'),
    path('shipment/status=<int:status>', views.filterShipment, name='filterShipment'),

]