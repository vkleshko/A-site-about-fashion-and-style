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
