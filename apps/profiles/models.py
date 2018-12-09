from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from email_hunter import EmailHunterClient
from starnavi.settings import EMAIL_HUNTER_KEY, CLEARBIT_KEY
from django.contrib.postgres.fields import JSONField
import clearbit

clearbit.key = CLEARBIT_KEY

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exists = models.BooleanField(default=False)
    additional_data = JSONField(null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
         client = EmailHunterClient(EMAIL_HUNTER_KEY)
         additional = clearbit.Enrichment.find(email=instance.email, stream=True)
         exists = client.exist(instance.email)
         p = Profile.objects.create(
            user=instance,
            additional_data=additional,
            exists=exists[0])
         p.save()
