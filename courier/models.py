from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Customer(TimeStampedModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Item(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


class Courier(TimeStampedModel):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


class FedEx(Courier):
    email = models.EmailField(max_length = 50)


class ShipmentStatus(models.TextChoices):
    RECEIVED = 1, _('RECEIVED')
    PROCESSING = 2, _('PROCESSING')
    FULFILLING = 3, _('FULFILLING')
    CANCELLED = 4, _('CANCELLED')


class Shipment(TimeStampedModel):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=1, choices=ShipmentStatus.choices, default=ShipmentStatus.RECEIVED)
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    courier = models.ForeignKey(
        Courier,
        on_delete=models.CASCADE
    )


class Waybill(TimeStampedModel):
    label = models.UUIDField(default=uuid.uuid4, editable=False)
    shipment = models.OneToOneField(
        Shipment,
        on_delete=models.CASCADE
    )


