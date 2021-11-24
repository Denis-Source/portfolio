from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=256)
    link = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name.capitalize()
