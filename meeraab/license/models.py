from django.db import models
from django.contrib.auth.models import User
from well.models import *
# Create your models here.

class ChargeAndCredit(models.Model):
    STATUS_CHOICES = (
        ('c', 'تایید‌ شده'),
        ('n', 'بررسی نشده'),
        ('d', 'رد شده'),
    )

    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ایجادکننده")
    well = models.OneToOneField(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل", related_name='ChargeAndCredit')

    annual_charge = models.IntegerField(null=True, blank=True,verbose_name="شارژ سالیانه")
    used_charge = models.IntegerField(null=True, blank=True,verbose_name="شارژ مصرف‌شده")
    remaining_charge = models.IntegerField(null=True, blank=True,verbose_name="شارژ باقی مانده")

    detail = models.TextField(verbose_name="جزییات بیشتر",null=True, blank=True)

    status = models.CharField(max_length=1, null=True, blank=True, choices = STATUS_CHOICES, verbose_name="وضعیت")


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "شارژ و اعتبار"
        verbose_name_plural = "شارژ‌ها و اعتبار‌ها"

    def __str__(self):
        return str(self.well)

class TechnicalCondition(models.Model):
    STATUS_CHOICES = (
        ('c', 'تایید‌ شده'),
        ('n', 'بررسی نشده'),
        ('d', 'رد شده'),
    )

    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ایجادکننده")
    well = models.OneToOneField(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل", related_name='TechnicalCondition')

    operation_license = models.BooleanField(default=False, verbose_name="پروانه‌ی بهره‌برداری معتبر می‌باشد")
    calibrated = models.BooleanField(default=False, verbose_name="کنتور کالیبره است")

    document = models.FileField(upload_to='documents',null=True, blank=True, verbose_name="مدرک")

    detail = models.TextField(verbose_name="جزییات بیشتر",null=True, blank=True)

    status = models.CharField(max_length=1, null=True, blank=True, choices = STATUS_CHOICES, verbose_name="وضعیت")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "وضعیت فنی"
        verbose_name_plural = "وضعیت‌های فنی"

    def __str__(self):
        return str(self.well)


class ModifyName(models.Model):
    STATUS_CHOICES = (
        ('c', 'تایید‌ شده'),
        ('n', 'بررسی نشده'),
        ('d', 'رد شده'),
    )

    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ایجادکننده")
    well = models.OneToOneField(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل", related_name='ModifyName')

    document = models.FileField(upload_to='documents',null=True, blank=True, verbose_name="مدارک")
    license = models.FileField(upload_to='documents',null=True, blank=True, verbose_name="پروانه")

    detail = models.TextField(verbose_name="جزییات بیشتر",null=True, blank=True)

    status = models.CharField(max_length=1, null=True, blank=True, choices = STATUS_CHOICES, verbose_name="وضعیت")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "اصلاح نام"
        verbose_name_plural = "اصلاح‌های نام"

    def __str__(self):
        return str(self.well)


class Commitment(models.Model):
    STATUS_CHOICES = (
        ('c', 'تایید‌ شده'),
        ('n', 'بررسی نشده'),
        ('d', 'رد شده'),
    )

    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ایجادکننده")
    well = models.OneToOneField(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل", related_name='Commitment')
    document = models.FileField(upload_to='documents',null=True, blank=True, verbose_name="مدارک")
    detail = models.TextField(verbose_name="جزییات بیشتر",null=True, blank=True)
    status = models.CharField(max_length=1, null=True, blank=True, choices = STATUS_CHOICES, verbose_name="وضعیت")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "تعهدنامه"
        verbose_name_plural = "تعهدنامه‌ها"

    def __str__(self):
        return str(self.well)

class Issuance(models.Model):
    STATUS_CHOICES = (
        ('c', 'تایید‌ شده'),
        ('n', 'بررسی نشده'),
        ('d', 'رد شده'),
    )

    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ایجادکننده")
    well = models.OneToOneField(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل", related_name='Issuance')

    annual_charge = models.IntegerField(null=True, blank=True,verbose_name="شارژ سالیانه")
    used_charge = models.IntegerField(null=True, blank=True,verbose_name="شارژ مصرف‌شده")
    remaining_charge = models.IntegerField(null=True, blank=True,verbose_name="شارژ باقی مانده")

    detail = models.TextField(verbose_name="جزییات بیشتر",null=True, blank=True)

    status = models.CharField(max_length=1, null=True, blank=True, choices = STATUS_CHOICES, verbose_name="وضعیت")


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "وضعیت نهایی‌شارژ و صدور فرم"
        verbose_name_plural = "وضعیت نهایی شارژ‌ها و صدور فرم‌ها"

    def __str__(self):
        return str(self.well)



    # TYPE_CHOICES = (
    #     ('k', 'خرید'),
    #     ('f', 'فروش'),
    # )
    # creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ایجاد کننده")
    # well = models.ForeignKey(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل")
    # type = models.CharField(max_length=1, null=True, blank=True, choices = TYPE_CHOICES, verbose_name="نوع معامله")
    #
    # amount = models.IntegerField(null=True, blank=True,verbose_name="مقدار معامله")
    # price = models.IntegerField(null=True, blank=True,verbose_name="مبلغ پیشنهادی",)
    #
    # status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    # slug = models.SlugField(max_length=100, blank=True, null=True, unique=True, verbose_name="آدرس")
    #
    # publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    # expire = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انقضا")
    #
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    #
    # class Meta:
    #     verbose_name = "دادوستد"
    #     verbose_name_plural = "دادوستد‌ها"
    #
    # def __str__(self):
    #     return str(self.type)+ '  '+str(self.well)
    #
    #
    # def jexpire(self):
    #     return jalali_converter(self.expire).split(',')[0]
    # jexpire.short_description = "تاریخ انقضا"
    #
    # def jpublish(self):
    #     return jalali_converter(self.publish).split(',')[0]
    # jpublish.short_description = "تاریخ انتشار"
