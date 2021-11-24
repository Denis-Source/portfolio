from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=256)
    priority = models.IntegerField()

    def __str__(self):
        return self.name.capitalize()
