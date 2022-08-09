# Generated by Django 4.0.5 on 2022-07-21 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('well', '0006_alter_abvand_owner_alter_chahvand_well_and_more'),
        ('transaction', '0002_transaction_to_abvand_alter_transaction_from_abvand'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='from_chahvand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fchv', to='well.chahvand', verbose_name='حساب چاه\u200cوندی فرستنده'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='from_well',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fw', to='well.chah', verbose_name='حساب چاه فرستنده'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='to_chahvand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tchv', to='well.chahvand', verbose_name='حساب چاه\u200cوندی گیرنده'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='to_well',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tw', to='well.chah', verbose_name='حساب چاه\u200c گیرنده'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='from_abvand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fab', to='well.abvand', verbose_name='حساب آب\u200cوندی فرستنده'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='to_abvand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tab', to='well.abvand', verbose_name='حساب آب\u200cوندی گیرنده'),
        ),
    ]