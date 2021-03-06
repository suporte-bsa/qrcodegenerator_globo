# Generated by Django 2.2.5 on 2019-09-15 02:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='URL',
            new_name='url',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(default=datetime.datetime.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.Post')),
            ],
        ),
    ]
