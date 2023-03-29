from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
from django.template.loader import render_to_string


class SendEmail():
    def __init__(self, template, subject, to) -> None:
        self.template = template
        self.subject = subject
        self.to = to
        self.send()

    def send(self):
        self.sendEmailNow(),
    
    def sendEmailNow(self):
        e = EmailMultiAlternatives(
            subject = self.subject,
            body = strip_tags(self.template),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to = self.to
            
        )
        e.attach_alternative(self.template, 'text/html')
        e.send()



def actionNotificationEmail(message, to, title=""):
    template = render_to_string("emails/action_notification.html", {'message':message, "title":title})

    s = SendEmail(template=template, subject=title, to=(to,"morganezekiah111@gmail.com"))

