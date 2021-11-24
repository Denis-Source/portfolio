from django.db import models


class Certificate(models.Model):
    name = models.CharField(max_length=64)
    priority = models.IntegerField()

    authority = models.CharField(max_length=64, blank=True, null=True)
    link = models.CharField(max_length=512, blank=True, null=True)
    download_link = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name.capitalize()
