from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from utils.EmailSender import actionNotificationEmail
from utils.randomString import GenerateRandomString

class Reciever(models.Model):
    full_name = models.CharField(null=False, blank=False, max_length=120)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(null=False, blank=False, max_length=120)
    location = models.CharField(null=False, blank=False,max_length=120)
    photo_image = models.ImageField(upload_to="reciever_images")

    def __str__(self) -> str:
        return self.email

    

    def get_absolute_url(self, *args, **kwargs):
        return reverse("updateReciever", kwargs={"pk":self.pk})



class Deliverer(models.Model):
    deliverer_name = models.CharField(max_length=510)
    deliverer_image = models.FileField(null=True, blank=True, upload_to="deliverer_images")


    def __str__(self) -> str:
        return self.deliverer_name


    def get_absolute_url(self, *args, **kwargs):
        return reverse("updateDeliverer",kwargs={"pk":self.pk})



class Location(models.Model):
    address = models.CharField(null=False, blank=False, max_length=120)
    note = models.CharField(null=False, blank=False,max_length=400)
    status = models.CharField(null=False, blank=False,max_length=400)
    date_created = models.DateField(default=timezone.now)


    class Meta:
        ordering=("-id",)



    def get_absolute_url(self, *args, **kwargs):
        return reverse("updateLocation", kwargs={"pk":self.pk})



    def __str__(self) -> str:
        return self.address
    

   

class Payment(models.Model):
    shipment_fee = models.IntegerField(null=True, blank=True)
    clearance_fee = models.IntegerField(null=True, blank=True)





    def __str__(self) -> str:
        return str(self.shipment_fee)

    

    @property
    def get_payment_total(self):
        total =0
        try:
            total = total + int(self.shipment_fee) 
        except:
            pass
        try:
            total = total +  int(self.clearance_fee)
        except:
            pass

        return int(total)

    
    def get_absolute_url(self):
        return reverse("updatePayment", kwargs={"pk":self.pk})



class Shipment(models.Model):
    weight = models.CharField(null=True, blank=True, max_length=120)
    quantity = models.CharField(null=True, blank=True, max_length=120)
    mode_of_shipment = models.CharField(null=True, blank=True, max_length=120)
    shipment_pick_up_date = models.CharField(null=True, blank=True, max_length=120)
    shipment_type = models.CharField(null=True, blank=True, max_length=120)
    comment = models.CharField(null=True, blank=True, max_length=120)
    uuid = models.TextField(null=False, blank=False, unique=True)
    registered_at_location = models.CharField(max_length=30, default="Texas")
    destination = models.CharField(null=True, blank=True, max_length=120)
    date_created = models.DateTimeField(default=timezone.now)

    reciever = models.ForeignKey(Reciever, on_delete=models.CASCADE)
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)



    def get_absolute_url(self):
        return reverse("updateShipment", kwargs={"pk": self.id})
    




    def __str__(self) -> str:
        return self.uuid
    

    @property
    def current_date(self):
        return timezone.now()




class SendEmail(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    reciever_email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.reciever_email

    
    

def assignUdid(instance):
    if  len(instance.uuid) < 1:
        uuid = GenerateRandomString.randomStringGenerator(7)
        try:
            Shipment.objects.get(uuid=uuid)
            assignUdid(instance)
        except:
            instance.uuid = uuid

def shipmentUuid(sender, instance, *args,**kwargs):
    assignUdid(instance)
    

def sendEmailDef(sender, instance, created, *args, **kwargs):
    if created:
        actionNotificationEmail(instance.message, instance.reciever_email,instance.subject )


pre_save.connect(shipmentUuid, sender=Shipment)
post_save.connect(sendEmailDef, sender=SendEmail)
