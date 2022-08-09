from django.db import models
from django.contrib.auth.models import User
from register_login.models import *
# Create your models here.

class Well(models.Model):
    USETYPE_CHOICES = (
        ('k', 'کشاورزی'),
        ('b', 'شرب'),
        ('b', 'صنعت'),
    )
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="مالک چاه")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="نام")
    license = models.CharField(max_length=200, null=True, blank=True, verbose_name="شماره پروانه")
    licensePic = models.FileField(upload_to='licensePic', verbose_name="عکس پروانه", blank=True, null=True)
    permitedAbdehi = models.CharField(max_length=200, null=True, blank=True, verbose_name="آبدهی مجاز")
    permitedWorkTime = models.CharField(max_length=200, null=True, blank=True, verbose_name="ساعت کارکرد مجاز")
    UTM = models.CharField(max_length=200, null=True, blank=True)
    useType=models.CharField(max_length=1, null=True, blank=True, choices = USETYPE_CHOICES, verbose_name="نوع بهرهبرداری")
    permitedUseInYear=models.CharField(max_length=200, null=True, blank=True, verbose_name="اجازه‌ی برداشت سالیانه")
    chargeInYear = models.CharField(max_length=200, null=True, blank=True, verbose_name="شارژ فعلی")

    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    slug = models.SlugField(max_length=100, blank=True, unique=True, verbose_name="آدرس")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "چاه"
        verbose_name_plural = "چاه‌ها"

    def __str__(self):
        return str(self.name)

class WellPhysicalInfo(models.Model):
    POMP_CHOICES =(
        ('k', 'شناور'),
        ('b', 'شفت و غلاف'),
    )
    well = models.OneToOneField(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل", related_name='WellPhysicalInfo')
    farmingType=models.CharField(max_length=200, null=True, blank=True, verbose_name="نوع کشت",)
    area=models.CharField(max_length=200, null=True, blank=True, verbose_name="مساحت")
    depth=models.CharField(max_length=200, null=True, blank=True, verbose_name="عمق چاه")
    power=models.CharField(max_length=200, null=True, blank=True, verbose_name="توان")
    abdehi=models.CharField(max_length=200, null=True, blank=True, verbose_name="آبدهی")
    pomp=models.CharField(max_length=1, null=True, blank=True, choices = POMP_CHOICES, verbose_name="نوع پمپ")
    buyCap=models.CharField(max_length=200, null=True, blank=True)
    sellCap=models.CharField(max_length=200, null=True, blank=True)
    wellCap=models.CharField(max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ویژگی‌های فیزیکی چاه"
        verbose_name_plural = "ویژگی‌های فیزیکی چاه‌ها"

    def __str__(self):
        return str(self.well)


class Chah(models.Model):
    accountID = models.CharField(max_length=200, verbose_name="شماره حساب")
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="مالک")
    well = models.ForeignKey(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل")

    currentcharge = models.CharField(max_length=200, null=True, blank=True, verbose_name="شارژ فعلی")

    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس ")
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "حساب چاه‌"
        verbose_name_plural = "حساب‌های چاه"

    def __str__(self):
        return self.accountID



class ChahVand(models.Model):
    accountID = models.CharField(max_length=200, verbose_name="شماره حساب")
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="مالک")
    well = models.ForeignKey(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه متصل")

    currentcharge = models.CharField(max_length=200, null=True, blank=True, verbose_name="شارژ فعلی")

    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس ")
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "حساب چاه‌وندی"
        verbose_name_plural = "حساب‌های چاه‌وندی"

    def __str__(self):
        return self.accountID
#
class AbVand(models.Model):
    accountID = models.CharField(max_length=200, verbose_name="شماره حساب")
    owner = models.ForeignKey(User, null=True, blank=True,on_delete=models.SET_NULL, verbose_name="مالک")
    currentcharge = models.CharField(max_length=200, null=True, blank=True, verbose_name="شارژ فعلی")

    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس ")
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "حساب آب‌وندی"
        verbose_name_plural = "حساب‌های آب‌وندی"

    def __str__(self):
        return self.accountID


class Beneficiary(models.Model):
    firstname = models.CharField(max_length=200, verbose_name="نام")
    lastname = models.CharField(max_length=200, verbose_name="نام خانوادگی")
    idNumber = models.CharField(max_length=200, verbose_name="کد ملی", null=True, blank=True)
    phoneNumber =  models.CharField(max_length=200, verbose_name="شماره تلفن", null=True, blank=True)
    well = models.ForeignKey(Well, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="چاه", related_name='Beneficiary')
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "بهره‌بردار چاه"
        verbose_name_plural = "بهره‌برداران چاه"

    def __str__(self):
        return str(self.well)
