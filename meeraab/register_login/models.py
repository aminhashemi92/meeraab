from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.
class Role(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL  ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان نقش")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name = "نقش"
        verbose_name_plural = "نقش‌ها"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE, verbose_name="کاربر")
    firstname = models.CharField(max_length=200, null=True, verbose_name="نام")
    lastname = models.CharField(max_length=200, null=True, verbose_name="نام‌خانوادگی")
    company = models.CharField(max_length=200, null=True, verbose_name="شرکت", blank=True)
    fatherName = models.CharField(max_length=200, null=True, verbose_name="نام پدر", blank=True)
    idNumber = models.CharField(max_length=200, null=True, verbose_name="کد ملی", blank=True)
    cardNumber = models.CharField(max_length=200, null=True, verbose_name="شماره شناسنامه", blank=True)
    birthDate = models.CharField(max_length=200, null=True, verbose_name="تاریخ تولد", blank=True)
    address = models.CharField(max_length=200, null=True, verbose_name="آدرس", blank=True)
    postCode = models.CharField(max_length=200, null=True, verbose_name="کد پستی", blank=True)
    email = models.EmailField(max_length=254, verbose_name="آدرس ایمیل", blank=True)
    confirmed = models.BooleanField(default=True, verbose_name="تایید حساب")
    role = models.ManyToManyField(Role, verbose_name="نقش", blank=True,)
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تاریخ ایجاد",  blank=True)
    pic = models.ImageField(upload_to="profileimages", null=True, verbose_name="تصویر", default="profileimages/profi.png", blank=True)
    sphone = models.CharField(max_length=200, null=True, verbose_name="تلفن ثابت", blank=True)
    mphone = models.CharField(max_length=200, null=True, verbose_name="تلفن همراه", blank=True)
    status = models.BooleanField(default=True, verbose_name="حساب کاربری فعال؟")

    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب‌های کاربری"

    def __str__(self):
        return str(self.user)

    def pic_tag(self):
        return format_html("<img style='width:55px;' src='{}'>".format(self.pic.url))
    pic_tag.short_description = "تصویر"

    def jdate_created(self):
        return jalali_converter(self.date_created)
    jdate_created.short_description = "تاریخ عضویت"
