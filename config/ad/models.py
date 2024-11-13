from django.db import models


def file_location(instance, filename, **kwargs):
    file_path = f"ad/{instance.title}-{filename}"
    return file_path

class Category(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    

class Ad(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image_base64 = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_ads")
    phone = models.CharField(max_length=13, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    number = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.title
    