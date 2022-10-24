from rest_framework.response import Response
from rest_framework.decorators import api_view
import uuid
import random

from .models import Waybill
from .models import Shipment


from .serializers import WaybillSerializer
from .serializers import ShipmentSerializer


@api_view(['POST'])
def createWaybill(request):
    label = None
    while True:
        try:
            label = uuid.uuid1(random.randint(0, 281474976710655))
            waybills = Waybill.objects.get(label=label)
        except Waybill.DoesNotExist:
            break

    shipment = Shipment.objects.get(pk=request.data['shipment'])
    waybill = Waybill(label=label, shipment=shipment)
    waybill.save()
    return Response(status=202)


@api_view(['GET'])
def WaybillLabel(request, id):
    try:
        waybill = Waybill.objects.get(pk=id)
        return Response(data={'label': waybill.label}, status=200)
    except Waybill.DoesNotExist:
        return Response(status=404)


@api_view(['GET'])
def shipmentStatus(request, id):
    try:
        shipment = Shipment.objects.get(pk=id)
        return Response(data={'status': shipment.status}, status=200)
    except Shipment.DoesNotExist:
        return Response(status=404)

@api_view(['GET'])
def filterShipment(request, status):
    try:
        shipments = Shipment.objects.filter(status=status)
        shipmentSerializer = ShipmentSerializer(shipments, many=True)
        return Response(data=shipmentSerializer.data, status=200)
    except Shipment.DoesNotExist:
        return Response(status=404)

