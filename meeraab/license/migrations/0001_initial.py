# Generated by Django 4.0.5 on 2022-08-02 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('well', '0010_alter_well_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Issuance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_license', models.BooleanField(default=False, verbose_name='پروانه\u200cی بهره\u200cبرداری معتبر می\u200cباشد')),
                ('calibrated', models.BooleanField(default=False, verbose_name='کنتور کالیبره است')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents', verbose_name='مدرک')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='جزییات بیشتر')),
                ('status', models.CharField(blank=True, choices=[('c', 'تایید\u200c شده'), ('n', 'بررسی نشده'), ('d', 'رد شده')], max_length=1, null=True, verbose_name='وضعیت')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ایجادکننده')),
                ('well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='TechnicalCondition', to='well.well', verbose_name='چاه متصل')),
            ],
        ),
        migrations.CreateModel(
            name='ModifyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents', verbose_name='مدارک')),
                ('license', models.FileField(blank=True, null=True, upload_to='documents', verbose_name='پروانه')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='جزییات بیشتر')),
                ('status', models.CharField(blank=True, choices=[('c', 'تایید\u200c شده'), ('n', 'بررسی نشده'), ('d', 'رد شده')], max_length=1, null=True, verbose_name='وضعیت')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ایجادکننده')),
                ('well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ModifyName', to='well.well', verbose_name='چاه متصل')),
            ],
        ),
        migrations.CreateModel(
            name='ChargeAndCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annual_charge', models.IntegerField(blank=True, null=True, verbose_name='شارژ سالیانه')),
                ('used_charge', models.IntegerField(blank=True, null=True, verbose_name='شارژ مصرف\u200cشده')),
                ('remaining_charge', models.IntegerField(blank=True, null=True, verbose_name='شارژ باقی مانده')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='جزییات بیشتر')),
                ('status', models.CharField(blank=True, choices=[('c', 'تایید\u200c شده'), ('n', 'بررسی نشده'), ('d', 'رد شده')], max_length=1, null=True, verbose_name='وضعیت')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ایجادکننده')),
                ('well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ChargeAndCredit', to='well.well', verbose_name='چاه متصل')),
            ],
        ),
    ]
