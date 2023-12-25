# Generated by Django 3.2.23 on 2023-12-25 00:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogforum', '0002_alter_author_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='v1701982014/lruym3fucw2jsqtj8smo.jpg', max_length=255, null=True, verbose_name='profile_pic'),
        ),
    ]
