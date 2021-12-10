from django.db import models


class Discipline(models.Model):
    """
    Discipline model
    Name field
    Priority field to place the category relatively others categories

    Optional link field to point the related git course (for example)
    """
    name = models.CharField(max_length=256)
    priority = models.IntegerField()

    link = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        """
        Returns Capitalised name of the discipline
        so the object in the admin panel is more readable
        """
        return self.name.capitalize()
