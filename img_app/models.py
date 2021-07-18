from django.db import models


class ImageModel(models.Model):
    """ Модель добавления изображения """
    image_id = models.IntegerField(primary_key=True)
    image_url = models.URLField(blank=True, verbose_name='Ссылка')
    image_loc = models.ImageField(blank=True, upload_to='images/', verbose_name='Файл')
    #created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    width_origin = models.PositiveIntegerField(verbose_name='Ширина', default=200)
    height_origin = models.PositiveIntegerField(verbose_name='Высота', default=200)

    @property
    def photo_url(self):
        if self.image_url and hasattr(self.image_url, 'url'):
            return self.image_url.url

    def save(self, *args, **kwargs):
        if not self.image_loc:
            self.image_loc = self.image_url
        super(ImageModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ImageUpdate(models.Model):
    """ Модель изменеия размеров изображения """
    width = models.PositiveIntegerField(blank=True, verbose_name='Ширина')
    height = models.PositiveIntegerField(blank=True, verbose_name='Высота')
    parent = models.ForeignKey(ImageModel, related_name='modified', on_delete=models.CASCADE)
