# Generated by Django 4.1.2 on 2022-11-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_expensisinpayment_summa_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensisinpayment',
            name='Summa_total',
            field=models.DecimalField(decimal_places=3, max_digits=10, max_length=30, null=True, verbose_name='Сумма итого'),
        ),
    ]
