from django.db import models

class ImageModel(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, verbose_name='Ссылка')
    # image_file = models.ImageField(blank=True, upload_to='images/')
    image_loc = models.ImageField(blank=True, upload_to='images/', verbose_name='Файл')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    # width_origin = models.PositiveIntegerField(verbose_name='Ширина')
    # height_origin = models.PositiveIntegerField(verbose_name='Высота')

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

    # def get_remote_image(self):
    #     if self.image_url and not self.image_file:
    #         result = urllib.request.urlopen(self.image_url)
    #         self.image_file.save(
    #             os.path.basename(self.image_url),
    #             File(open(result[0]))
    #         )
    #         self.save()

    # def get_img(self):
    #
    #     url = self.image_url
    #     try:
    #         resp = requests.get(url, stream=True).raw
    #     except requests.exceptions.RequestException as e:
    #         sys.exit(1)
    #     try:
    #         img = Image.open(resp)
    #     except IOError:
    #         print("Unable to open image")
    #         sys.exit(1)
    #     return img.save(self.image_file, 'jpeg')
