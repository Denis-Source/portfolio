from django.db import models


class Category(models.Model):
    """
    Category model
    name field
    priority field to place the category relatively others categories

    Is needed to sort projects
    Interlinked with Project model with one to many relationship
    """
    name = models.CharField(max_length=64)
    priority = models.IntegerField()

    def __str__(self):
        """
        Returns Capitalised name of the category
        so the object in the admin panel is more readable
        """
        return self.name.capitalize()
