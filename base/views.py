from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from base.forms import DelivererForm, LocationForm, PaymentForm, RecieverForm, SendEmailForm, ShipmentForm
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Deliverer, Location, Payment, Reciever, Shipment
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")




def about(request):
    return render(request, "about.html")



@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard/index.html")




class TrackShipment(View):
    def get(self, request, tracking_uuid):
        try:
            shipment = Shipment.objects.get(uuid=tracking_uuid)
        except:
            return HttpResponse("Shipment with this UUID does not exist")
        locations = shipment.location
        firstLocation = shipment.location.all()[0]
        locations = locations.exclude(id=firstLocation.id)
     

        return render(request, "track_shipment.html", {"shipment":shipment,"locations":locations})



class PrintInvoice(View):
    def get(self, request, tracking_uuid):
        try:
            shipment = Shipment.objects.get(uuid=tracking_uuid)
        except:
            return HttpResponse("Shipment with this UUID does not exist")
        return render(request, "print_invoice.html", {"shipment":shipment})







###SHIPMENT###
class CreateShipment(LoginRequiredMixin, CreateView):
    template_name = "dashboard/shipment/create_shipment.html"
    queryset = Shipment
    form_class =ShipmentForm



class UpdateShipment(LoginRequiredMixin, UpdateView):
    template_name="dashboard/shipment/update_shipment.html"
    model=Shipment
    form_class = ShipmentForm
    context_object_name="shipment"



class ListShipment(LoginRequiredMixin,ListView):
    template_name="dashboard/shipment/list_shipment.html"
    model=Shipment
    context_object_name="shipments"


class DeleteShipment(View):
    def post(self, request):
        id = request.POST.get("shipment_id")
        try:
            shipment = Shipment.objects.get(id=id)
        except Shipment.DoesNotExist as e:
            return HttpResponse("Shipment With this ID does not exist")
        
        shipment.delete()
        return redirect("dashboard")





###LOCATION VIEW ###
class CreateLocation(LoginRequiredMixin, CreateView):
    template_name="dashboard/location/create_location.html"
    queryset=Location
    form_class = LocationForm

class UpdateLocation(LoginRequiredMixin, UpdateView):
    template_name="dashboard/location/update_location.html"
    model=Location
    context_object_name="location"
    fields = "__all__"


class ListLocation(LoginRequiredMixin,ListView):
    template_name="dashboard/location/list_location.html"
    model=Location
    context_object_name="locations"

class DeleteLocation(View):
    def post(self, request):
        id = request.POST.get("location_id")
        try:
            location = Location.objects.get(id=id)
        except Location.DoesNotExist as e:
            return HttpResponse("Location With this ID does not exist")
        
        location.delete()
        return redirect("dashboard")








###RECIEVER VIEW ###

class CreateReciever(LoginRequiredMixin, CreateView):
    template_name="dashboard/reciever/create_reciever.html"
    queryset=Reciever
    form_class = RecieverForm

class UpdateReciever(LoginRequiredMixin, UpdateView):
    template_name="dashboard/reciever/update_reciever.html"
    model=Reciever
    fields ="__all__"

    


class ListReciever(LoginRequiredMixin,ListView):
    template_name="dashboard/reciever/list_reciever.html"
    model=Reciever
    context_object_name="recievers"

class DeleteReciever(View):
    def post(self, request):
        id = request.POST.get("reciever_id")
        try:
            reciever = Reciever.objects.get(id=id)
        except Location.DoesNotExist as e:
            return HttpResponse("Receiever With this ID does not exist")
        
        reciever.delete()
        return redirect("dashboard")



    




###DELIVERER VIEW ###

class CreateDeliverer(LoginRequiredMixin, CreateView):
    template_name="dashboard/deciever/create_deliverer.html"
    queryset=Deliverer
    form_class = DelivererForm


class UpdateDeliverer(LoginRequiredMixin, UpdateView):
    template_name="dashboard/deciever/update_deliverer.html"
    model=Deliverer
    object_name="deliverer"
    fields = "__all__"



    

class ListDeliverer(LoginRequiredMixin,ListView):
    template_name="dashboard/deciever/list_deliverer.html"
    model=Deliverer
    context_object_name="deliverers"

class DeleteDeliverer(View):
    def post(self, request):
        id = request.POST.get("deliverer_id")
        try:
            deliverer = Deliverer.objects.get(id=id)
        except Location.DoesNotExist as e:
            return HttpResponse("Receiever With this ID does not exist")
        
        deliverer.delete()
        return redirect("dashboard")







###PAYMENT###
class CreatePayment(LoginRequiredMixin, CreateView):
    template_name = "dashboard/payment/create_payment.html"
    queryset = Payment
    form_class =PaymentForm



class UpdatePayment(LoginRequiredMixin, UpdateView):
    template_name="dashboard/payment/update_payment.html"
    model=Payment
    form_class = PaymentForm
    context_object_name="payment"



class ListPayment(LoginRequiredMixin,ListView):
    template_name="dashboard/payment/list_payment.html"
    model=Payment
    context_object_name="payments"


class DeletePayment(View):
    def post(self, request):
        id = request.POST.get("payment_id")
        try:
            payment = Payment.objects.get(id=id)
        except Payment.DoesNotExist as e:
            return HttpResponse("Payment With this ID does not exist")
        
        payment.delete()
        return redirect("dashboard")





class SendEmailView(CreateView):
    template_name="dashboard/send_email.html"
    form_class = SendEmailForm
    success_url="emailSentSuccessfully"


@login_required
def emailSentSuccessfully(request):
    return HttpResponse(f'''Email Sent successfully, <a href='{reverse("dashboard")}'>return to dashboard</a>''')