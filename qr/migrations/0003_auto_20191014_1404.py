# Generated by Django 2.2.6 on 2019-10-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_auto_20190914_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]
