from django.db import models
from django.utils.text import slugify

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    image2 = models.ImageField(upload_to='news/', blank=True, null=True)
    image3 = models.ImageField(upload_to='news/', blank=True, null=True)
    image4 = models.ImageField(upload_to='news/', blank=True, null=True)
    image5 = models.ImageField(upload_to='news/', blank=True, null=True)
    image6 = models.ImageField(upload_to='news/', blank=True, null=True)
    image7 = models.ImageField(upload_to='news/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Schedule(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="schedule_images/", blank=True)