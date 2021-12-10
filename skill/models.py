from django.db import models


class Skill(models.Model):
    """
    Skill model
    Name field
    Priority field to place the category relatively others categories
    """
    name = models.CharField(max_length=256)
    priority = models.IntegerField()

    def __str__(self):
        """
        Returns Capitalised name of the discipline
        so the object in the admin panel is more readable
        """
        return self.name.capitalize()
