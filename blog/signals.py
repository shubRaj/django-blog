from django.dispatch import receiver
from django.core.signals import request_finished
from django.contrib.auth.models import User
@receiver(request_finished)
def profile_log(sender,**kwargs):
    pass