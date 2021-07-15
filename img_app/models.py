import os

import urllib.request
import requests

from django.contrib.sites import requests
from django.db import models
from django.core.files import File


class ImageModel(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, verbose_name='Ссылка')
    #image_file = models.ImageField(blank=True, upload_to='images/')
    image_loc = models.ImageField(blank=True, upload_to='images/', verbose_name='Файл')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    # width_origin = models.PositiveIntegerField(verbose_name='Ширина')
    # height_origin = models.PositiveIntegerField(verbose_name='Высота')

    # def get_remote_image(self):
    #     if self.image_url and not self.image_file:
    #         result = urllib.urlretrieve(self.image_url)
    #         self.image_file.save(
    #             os.path.basename(self.image_url),
    #             File(open(result[0]))
    #         )
    #         self.save()
    def save_2(self):
        p = requests.get(self.image_url)
        out = open('MEDIA_URL' + 'self.image_url' + '.jpg', "wb")
        out.write(p.content)
        out.close()
        self.save()

    def __str__(self):
        return self.title
