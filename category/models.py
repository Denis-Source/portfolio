from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    priority = models.IntegerField()

    def __str__(self):
        return self.name.capitalize()
