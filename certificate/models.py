from django.db import models


class Certificate(models.Model):
    """
    Certificate model
    name field to display skills proven by the certificate
    priority field to place the certificate relatively to others
    authority field to specify the organisation that gave the certificate

    file field to upload and show the certificate as a part of the sit
    link field substitutes file field with a link to the certificate

    if file is provided link is shown to that file, link field in that case is redundant
    """
    name = models.CharField(max_length=64)
    priority = models.IntegerField()

    authority = models.CharField(max_length=64, blank=True, null=True)
    file = models.FileField(upload_to="certificates/", blank=True, null=True)
    link = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        """
        Returns Capitalised name of the certificate
        so the object in the admin panel is more readable
        """
        return self.name.capitalize()
