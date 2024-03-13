import os
import uuid

from django.db import models
from django.utils.text import slugify


def item_image_file_path(instance, file_name):
    _, extension = os.path.splitext(file_name)
    file_path = f"{slugify(instance.name)}-{uuid.uuid4()}.{extension}"
    return os.path.join("uploads/items/", file_path)


class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    picture = models.ImageField(upload_to=item_image_file_path)

    def __str__(self):
        return f"{self.name} {self.description}"


class Category(models.Model):
    CATEGORY_CHOICES = (
        ("Business", ("Business")),
        ("Casual", ("Casual")),
        ("Formal", ("Formal")),
        ("Lingerie", ("Lingerie")),
        ("Sports", ("Sports")),
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.name
