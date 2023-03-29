from django.urls import path
from base.forms import SendEmailForm

from base.views import CreateDeliverer, CreateLocation, CreateReciever, CreateShipment, DeleteDeliverer, DeleteReciever, DeleteShipment, ListDeliverer, ListReciever, ListShipment, SendEmailView, UpdateDeliverer, UpdateLocation, UpdateReciever, UpdateShipment, dashboard,DeleteLocation,ListLocation, ListPayment, DeletePayment, UpdatePayment, CreatePayment, emailSentSuccessfully


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("createShipment", CreateShipment.as_view(), name="createShipment"),
    path("listShipment", ListShipment.as_view(), name="listShipment"),
    path("deleteShipment", DeleteShipment.as_view(), name="deleteShipment"),
    path("updateShipment/<pk>", UpdateShipment.as_view(), name="updateShipment"),






    path("createLocation", CreateLocation.as_view(), name="createLocation"),
    path("deleteLocation", DeleteLocation.as_view(), name="deleteLocation"),
    path("listLocation", ListLocation.as_view(), name="listLocation"),
    path("updateLocation/<pk>", UpdateLocation.as_view(), name="updateLocation"),





    path("createReciever", CreateReciever.as_view(), name="createReciever"),
    path("deleteReciever", DeleteReciever.as_view(), name="deleteReciever"),
    path("listReciever", ListReciever.as_view(), name="listReciever"),
    path("updateReciever/<pk>", UpdateReciever.as_view(), name="updateReciever"),





    path("createDeliverer", CreateDeliverer.as_view(), name="createDeliverer"),
    path("deleteDeliverer", DeleteDeliverer.as_view(), name="deleteDeliverer"),
    path("listDeliverer", ListDeliverer.as_view(), name="listDeliverer"),
    path("updateDeliverer/<pk>", UpdateDeliverer.as_view(), name="updateDeliverer"),



    ###PAYMENT###
    path("createPayment", CreatePayment.as_view(), name="createPayment"),
    path("listPayment", ListPayment.as_view(), name="listPayment"),
    path("deletePayment", DeletePayment.as_view(), name="deletePayment"),
    path("updatePayment/<pk>", UpdatePayment.as_view(), name="updatePayment"),


    ##SENDEMAIL##
    path("sendEmail",SendEmailView.as_view(), name="sendEmailView"),
    path("emailSentSuccessfully", emailSentSuccessfully, name="emailSentSuccessfully")

]
