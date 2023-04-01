from base.models import Shipment, Location,Deliverer, Reciever


def app(request):
    shipments = Shipment.objects.all()
    locations = Location.objects.all()
    deliverers = Deliverer.objects.all()
    recievers = Reciever.objects.all()

    return {
        "app_name":"ZoomCourier",
        "shipments":shipments,
        "locations":locations,
        "deliverers":deliverers,
        "recievers":recievers,
        "phone_number":"+1(863)417-2285",
        "email":"support@cargointransit.online",
        "address":'''A108 Adam Street
New York, NY 535022
United States'''
    }