from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=256)
