from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.FileField(blank=True, upload_to='images/', verbose_name='Ссылка')
    image_loc = models.ImageField(blank=True, upload_to='images/', verbose_name='Файл')

    def __str__(self):
        return self.title



