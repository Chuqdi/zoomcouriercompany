
from django.contrib import admin
from django.urls import path, include
from base.views import PrintInvoice, TrackShipment, index, contact, about, services
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path("", index, name="index"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("services", services, name="services"),
    path("trackShipment/<tracking_uuid>", TrackShipment.as_view(), name="trackShipment"),
    path("print_invoice/<tracking_uuid>", PrintInvoice.as_view(), name="print_invoice"),

    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("dashboard/",include("base.url_dashboard")),
    path("print_invoice/<tracking_uuid>", PrintInvoice.as_view(), name="print_invoice"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)