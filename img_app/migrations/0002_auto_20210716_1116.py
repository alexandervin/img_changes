# Generated by Django 3.2.5 on 2021-07-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='height_origin',
            field=models.PositiveIntegerField(default=200, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='width_origin',
            field=models.PositiveIntegerField(default=200, verbose_name='Ширина'),
        ),
    ]