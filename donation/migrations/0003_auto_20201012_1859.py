# Generated by Django 3.1.1 on 2020-10-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_resourcepost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcepost',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='staticfiles'),
        ),
    ]
