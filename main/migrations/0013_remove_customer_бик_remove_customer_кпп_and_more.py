# Generated by Django 4.1.2 on 2022-11-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_customer_ks_alter_customer_бик_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='БИК',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='КПП',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Р/С',
        ),
        migrations.AddField(
            model_name='customer',
            name='Bik',
            field=models.IntegerField(null=True, verbose_name='БИК'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Kpp',
            field=models.IntegerField(null=True, verbose_name='КПП'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Rs',
            field=models.IntegerField(null=True, verbose_name='Р/С'),
        ),
    ]
