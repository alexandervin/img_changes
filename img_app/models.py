from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, verbose_name='Ссылка')
    image_loc = models.ImageField(blank=True,upload_to='images/', verbose_name='Файл')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title



