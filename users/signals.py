from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


''' create profile function function which will run every time a user is created'''

'''
In here we have a sender(sender=user) and a signal (post_save) so when a user is saved and send the signal and the signal is going to 
be recived by @reciever and the the create profile function is the reciever takes all the arguments that the post_save signal is passed
to it.
if a user is creared then a new profile will be created

'''


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


'''after creating this signals .py file make changes in apps.py and __init__.py file
we have to add in line to __init__.py file we have added our "appname" to your INSTALLED_APPS instead of "appname.apps.AppnameConfig"'''