# Generated by Django 4.0.5 on 2022-06-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, null=True, verbose_name='نام')),
                ('lastname', models.CharField(max_length=200, null=True, verbose_name='نام\u200cخانوادگی')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='عنوان پیام')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
                ('role', models.CharField(choices=[('k', 'رسانه\u200cخواه'), ('b', 'رسانه\u200cدار')], max_length=1, null=True, verbose_name='نقش')),
                ('mphone', models.CharField(max_length=200, null=True, verbose_name='تلفن')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='آدرس آی\u200cپی')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'فرم ارتباط با ما',
                'verbose_name_plural': 'فرم\u200cهای ارتباط با ما',
            },
        ),
    ]
