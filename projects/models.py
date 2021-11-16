from django.db import models
from category.models import Category


class Project(models.Model):
    name = models.CharField(max_length=64)

    priority = models.IntegerField()

    description = models.CharField(max_length=256)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    link = models.CharField(max_length=512)
    image = models.ImageField(upload_to="projects/")


    def __str__(self):
        return self.name.capitalize()
