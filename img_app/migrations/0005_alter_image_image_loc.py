# Generated by Django 3.2.5 on 2021-07-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_app', '0004_alter_image_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_loc',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Файл'),
        ),
    ]
