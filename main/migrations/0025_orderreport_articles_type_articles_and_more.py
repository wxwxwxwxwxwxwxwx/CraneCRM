# Generated by Django 4.1.3 on 2022-12-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_articles_unit_articles_alter_articles_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_at', models.DateField(blank=True, default=None, null=True, verbose_name='Дата  от')),
                ('date_to', models.DateField(blank=True, default=None, null=True, verbose_name='Дата  до')),
            ],
            options={
                'verbose_name': 'План/Факт анализ',
                'verbose_name_plural': 'План/Факт анализ',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='Type_articles',
            field=models.BooleanField(default=False, verbose_name='Материалы'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Full_director',
            field=models.CharField(max_length=200, null=True, verbose_name='Директор'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_date',
            field=models.DateTimeField(null=True, verbose_name='Дата документа'),
        ),
        migrations.AlterField(
            model_name='expensisindocument',
            name='Summaclient',
            field=models.FloatField(null=True, verbose_name='Сумма для клиента'),
        ),
        migrations.AlterField(
            model_name='expensisindocument',
            name='Volume',
            field=models.FloatField(null=True, verbose_name='Объем'),
        ),
    ]
