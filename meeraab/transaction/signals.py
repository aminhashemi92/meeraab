from .models import *
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

import string
import random

@receiver(post_save, sender=Transaction)
def update_credit(sender, instance, created, *args, **kwargs):
    if created:
        amount = instance.amount
        bucket = instance.bucket
        type = instance.type

        if type == 'aa':
            send = instance.from_abvand
            receive = instance.to_abvand
            try:
                lastsend = Credit.objects.filter(bucket=bucket, abvand=send).last()
            except Credit.DoesNotExist:
                lastsend = None

            try:
                lastreceive = Credit.objects.filter(bucket=bucket, abvand=receive).last()
            except Credit.DoesNotExist:
                lastreceive = None

            if lastsend:
                lastsendcredit = lastsend.credit
            else:
                lastsendcredit = 0

            if lastreceive:
                lastreceivecredit = lastreceive.credit
            else:
                lastreceivecredit = 0

            Credit.objects.create(bucket=bucket, credit=lastsendcredit-amount, precredit=lastsendcredit, abvand=send,)
            Credit.objects.create(bucket=bucket, credit=lastreceivecredit+amount, precredit=lastreceivecredit, abvand=receive,)

        elif type == 'ca':
            send = instance.from_chahvand
            receive = instance.to_abvand

            try:
                lastsend = Credit.objects.filter(bucket=bucket, chahvand=send).last()
            except Credit.DoesNotExist:
                lastsend = None

            try:
                lastreceive = Credit.objects.filter(bucket=bucket, abvand=receive).last()
            except Credit.DoesNotExist:
                lastreceive = None

            if lastsend:
                lastsendcredit = lastsend.credit
            else:
                lastsendcredit = 0

            if lastreceive:
                lastreceivecredit = lastreceive.credit
            else:
                lastreceivecredit = 0

            Credit.objects.create(bucket=bucket, credit=lastsendcredit-amount, precredit=lastsendcredit, chahvand=send,)
            Credit.objects.create(bucket=bucket, credit=lastreceivecredit+amount, precredit=lastreceivecredit, abvand=receive,)


        elif type == 'ac':
            send = instance.from_abvand
            receive = instance.to_chahvand

            try:
                lastsend = Credit.objects.filter(bucket=bucket, abvand=send).last()
            except Credit.DoesNotExist:
                lastsend = None

            try:
                lastreceive = Credit.objects.filter(bucket=bucket, chahvand=receive).last()
            except Credit.DoesNotExist:
                lastreceive = None


            if lastsend:
                lastsendcredit = lastsend.credit
            else:
                lastsendcredit = 0

            if lastreceive:
                lastreceivecredit = lastreceive.credit
            else:
                lastreceivecredit = 0


            Credit.objects.create(bucket=bucket, credit=lastsendcredit-amount, precredit=lastsendcredit, abvand=send,)
            Credit.objects.create(bucket=bucket, credit=lastreceivecredit+amount, precredit=lastreceivecredit, chahvand=receive,)


        elif type == 'cw':
            send = instance.from_chahvand
            receive = instance.to_well

            try:
                lastsend = Credit.objects.filter(bucket=bucket, chahvand=send).last()
            except Credit.DoesNotExist:
                lastsend = None

            try:
                lastreceive = Credit.objects.filter(bucket=bucket, well=receive).last()
            except Credit.DoesNotExist:
                lastreceive = None


            if lastsend:
                lastsendcredit = lastsend.credit
            else:
                lastsendcredit = 0

            if lastreceive:
                lastreceivecredit = lastreceive.credit
            else:
                lastreceivecredit = 0


            Credit.objects.create(bucket=bucket, credit=lastsendcredit-amount, precredit=lastsendcredit, chahvand=send,)
            Credit.objects.create(bucket=bucket, credit=lastreceivecredit+amount, precredit=lastreceivecredit, well=receive,)


        elif type == 'wc':
            send = instance.from_well
            receive = instance.to_chahvand

            try:
                lastsend = Credit.objects.filter(bucket=bucket, well=send).last()
            except Credit.DoesNotExist:
                lastsend = None

            try:
                lastreceive = Credit.objects.filter(bucket=bucket, chahvand=receive).last()
            except Credit.DoesNotExist:
                lastreceive = None


            if lastsend:
                lastsendcredit = lastsend.credit
            else:
                lastsendcredit = 0

            if lastreceive:
                lastreceivecredit = lastreceive.credit
            else:
                lastreceivecredit = 0


            Credit.objects.create(bucket=bucket, credit=lastsendcredit-amount, precredit=lastsendcredit, well=send,)
            Credit.objects.create(bucket=bucket, credit=lastreceivecredit+amount, precredit=lastreceivecredit, chahvand=receive,)





#     if created == False:
#         profile = instance.profile
#         profile.mphone =  instance.phone
#         profile.save()

@receiver(pre_save, sender=Transaction)
def create_bucket(sender, instance, *args, **kwargs):
    if instance.type=='wc' and not instance.bucket:
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        obj = Bucket.objects.create(name=name, source_well=instance.from_well.well)
        instance.bucket = obj
