# Generated by Django 4.0.5 on 2022-08-02 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('well', '0010_alter_well_name'),
        ('license', '0003_alter_chargeandcredit_well_alter_modifyname_well_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modifyname',
            name='well',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ModifyName', to='well.well', verbose_name='چاه متصل'),
        ),
    ]