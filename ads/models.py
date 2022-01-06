from django.db import models
from config.mixins import TranslateMixin


class Category(TranslateMixin, models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    image = models.ImageField()
    added_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

