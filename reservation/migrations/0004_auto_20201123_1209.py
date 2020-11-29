# Generated by Django 3.1.1 on 2020-11-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20201123_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationpost',
            name='reservationstatus',
            field=models.IntegerField(choices=[(1, 'accept'), (2, 'reject'), (3, 'pending')], default=3),
        ),
    ]
