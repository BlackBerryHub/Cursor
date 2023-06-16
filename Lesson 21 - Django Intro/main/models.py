import hashlib
import os

from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SliderItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, editable=False)
    image = models.ImageField(upload_to="uploads/")


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate SHA256 hash from the image URL
        hash_object = hashlib.sha256(self.image.url.encode())
        link_hash = hash_object.hexdigest()

        # Assign the hash as the link
        self.link = link_hash
        self.image.name = f"{link_hash}.jpg"

        super().save(*args, **kwargs)
