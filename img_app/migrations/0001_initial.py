# Generated by Django 3.2.5 on 2021-07-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image_url', models.ImageField(blank=True, upload_to='images/', verbose_name='Ссылка')),
                ('image_loc', models.ImageField(blank=True, upload_to='images/', verbose_name='Файл')),
            ],
        ),
    ]