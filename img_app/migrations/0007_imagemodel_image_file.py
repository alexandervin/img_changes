# Generated by Django 3.2.5 on 2021-07-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_app', '0006_remove_imagemodel_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='image_file',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
