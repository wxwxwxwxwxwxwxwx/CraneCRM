# Generated by Django 4.1.3 on 2022-12-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_articles_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='Unit_articles',
            field=models.CharField(max_length=30, null=True, verbose_name='Ед. изм'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
    ]
