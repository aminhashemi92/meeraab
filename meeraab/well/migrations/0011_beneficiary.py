# Generated by Django 4.0.5 on 2022-08-04 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('well', '0010_alter_well_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('beneficiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='بهره\u200cبردار')),
                ('well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='well.well', verbose_name='چاه')),
            ],
            options={
                'verbose_name': 'بهره\u200cبردار چاه',
                'verbose_name_plural': 'بهره\u200cبرداران چاه',
            },
        ),
    ]