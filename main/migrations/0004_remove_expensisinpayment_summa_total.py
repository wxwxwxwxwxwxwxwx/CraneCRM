# Generated by Django 4.1.2 on 2022-11-02 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_expensisinpayment_summa_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensisinpayment',
            name='Summa_total',
        ),
    ]
