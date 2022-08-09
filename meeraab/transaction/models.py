from django.db import models
from well.models import *

# Create your models here.

class Bucket(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="نوع")
    source_well = models.ForeignKey(Well,null=True, blank=True, verbose_name="حساب چاه", on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "نوع آب"
        verbose_name_plural = "انواع آب‌ها"

    def __str__(self):
        return str(self.name)



class Transaction(models.Model):
    TYPE_CHOICES = (
        ('aa', 'آب‌وندی به آب‌وندی'),
        ('ca', 'چاه‌وندی به آب‌وندی'),
        ('ac', 'آب‌وندی به چاه‌وندی'),
        ('cw', 'چاه‌وندی به چاه'),
        ('wc', 'چاه‌ به چاه‌وندی'),
    )
    type = models.CharField(max_length=2, null=True, blank=True, choices = TYPE_CHOICES, verbose_name="نوع معامله")
    back = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,verbose_name='برگشتی')
    bucket = models.ForeignKey(Bucket,null=True, blank=True, verbose_name="دلو", on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField(null=True, blank=True, verbose_name="مقدار")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    from_abvand = models.ForeignKey(AbVand, blank=True, null=True, verbose_name="حساب آب‌وندی فرستنده", on_delete=models.SET_NULL, related_name='fab')
    to_abvand = models.ForeignKey(AbVand, blank=True, null=True, verbose_name="حساب آب‌وندی گیرنده", on_delete=models.SET_NULL, related_name='tab')

    from_chahvand = models.ForeignKey(ChahVand, blank=True, null=True, verbose_name="حساب چاه‌وندی فرستنده", on_delete=models.SET_NULL, related_name='fchv')
    to_chahvand = models.ForeignKey(ChahVand, blank=True, null=True, verbose_name="حساب چاه‌وندی گیرنده", on_delete=models.SET_NULL, related_name='tchv')

    from_well = models.ForeignKey(Chah, blank=True, null=True, verbose_name="حساب چاه فرستنده", on_delete=models.SET_NULL, related_name='fw')
    to_well = models.ForeignKey(Chah, blank=True, null=True, verbose_name="حساب چاه‌ گیرنده", on_delete=models.SET_NULL, related_name='tw')

    class Meta:
        verbose_name = "انتقال"
        verbose_name_plural = "انتقال‌ها"

    def __str__(self):
        return str(self.type)


class Credit(models.Model):
    bucket = models.ForeignKey(Bucket,null=True, blank=True, verbose_name="دلو", on_delete=models.SET_NULL)

    credit = models.IntegerField(null=True, blank=True, verbose_name="موجودی فعلی")
    precredit = models.IntegerField(null=True, blank=True, verbose_name="موجودی قبلی")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    abvand = models.ForeignKey(AbVand, blank=True, null=True, verbose_name="حساب آب‌وندی متصل", on_delete=models.SET_NULL, related_name='Credit')

    chahvand = models.ForeignKey(ChahVand, blank=True, null=True, verbose_name="حساب چاه‌وندی متصل", on_delete=models.SET_NULL, related_name='Credit')

    well = models.ForeignKey(Chah, blank=True, null=True, verbose_name="حساب چاه متصل", on_delete=models.SET_NULL, related_name='Credit')


    class Meta:
        verbose_name = "مانده حساب"
        verbose_name_plural = "مانده حساب‌ها"

    def __str__(self):
        return str(self.credit)
