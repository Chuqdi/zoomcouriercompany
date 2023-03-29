from django import forms
from .models import Payment, SendEmail, Shipment,  Location, Reciever, Deliverer




MODE_OF_SHIPMENT_CHOICES = [('Air Fleight', 'Air Fleight'), ('Ocean Fleight', 'Ocean Fleight'), ('Land Fleight', 'Land Fleight'), ]


SHIPMENT_LOCATION_STATUS = [("In Progress","In Progress"), ("Delayed","Delayed"),("On Hold","On Hold")]


TYPE_OF_SHIPMENT_CHOICES = [('Personal', 'Personal'), ('Commercial', 'Commercial'), ('Other', 'Other'), ]

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = (
            "weight",
            "quantity",
            "mode_of_shipment",
            "shipment_pick_up_date",
            "shipment_type",
            "comment",
            "destination",
            "registered_at_location",
            "reciever",
            "deliverer",
            "location",
            "payments"
        )

        widgets = {
            'mode_of_shipment': forms.Select(choices=MODE_OF_SHIPMENT_CHOICES),
            "shipment_type":forms.Select(choices=TYPE_OF_SHIPMENT_CHOICES)
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ("address", "note", "status")
      

        widgets ={
            "status":forms.Select(choices=SHIPMENT_LOCATION_STATUS)
        }


class RecieverForm(forms.ModelForm):
    class Meta:
        model = Reciever
        fields = "__all__"



class DelivererForm(forms.ModelForm):
    class Meta:
        model = Deliverer
        fields = "__all__"



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"




class SendEmailForm(forms.ModelForm):
    class Meta:
        model = SendEmail
        fields ="__all__"