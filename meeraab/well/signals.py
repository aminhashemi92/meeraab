from .models import *
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify



@receiver(pre_save, sender=Well)
def slug_maker(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.license)


#
@receiver(post_save, sender=Well)
def create_wellphysical(sender, instance, created, *args, **kwargs):
    # WellPhysicalInfo.objects.create(well=instance)
    if created:
        WellPhysicalInfo.objects.create(well=instance)


#     if created == False:
#         profile = instance.profile
#         profile.mphone =  instance.phone
#         profile.save()
