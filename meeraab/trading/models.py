from django.db import models
from django.contrib.auth.models import User
from register_login.models import *
from well.models import *
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.

class Trade(models.Model):
    TYPE_CHOICES = (
        ('k', 'خرید'),
        ('f', 'فروش'),
    )
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ایجاد کننده")
    well = models.ForeignKey(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل")
    type = models.CharField(max_length=1, null=True, blank=True, choices = TYPE_CHOICES, verbose_name="نوع معامله")

    amount = models.IntegerField(null=True, blank=True,verbose_name="مقدار معامله")
    price = models.IntegerField(null=True, blank=True,verbose_name="مبلغ پیشنهادی",)

    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True, verbose_name="آدرس")

    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    expire = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انقضا")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "دادوستد"
        verbose_name_plural = "دادوستد‌ها"

    def __str__(self):
        return str(self.type)+ '  '+str(self.well)


    def jexpire(self):
        return jalali_converter(self.expire).split(',')[0]
    jexpire.short_description = "تاریخ انقضا"

    def jpublish(self):
        return jalali_converter(self.publish).split(',')[0]
    jpublish.short_description = "تاریخ انتشار"
