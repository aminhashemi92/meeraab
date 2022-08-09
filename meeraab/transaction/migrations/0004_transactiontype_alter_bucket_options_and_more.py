# Generated by Django 4.0.5 on 2022-07-21 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_transaction_from_chahvand_transaction_from_well_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='آدرس')),
            ],
            options={
                'verbose_name': 'نوع معامله',
                'verbose_name_plural': 'انواع معامله',
            },
        ),
        migrations.AlterModelOptions(
            name='bucket',
            options={'verbose_name': 'نوع آب', 'verbose_name_plural': 'انواع آب\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'انتقال', 'verbose_name_plural': 'انتقال\u200cها'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transaction.transactiontype', verbose_name='نوع معامله'),
        ),
    ]
