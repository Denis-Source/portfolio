from django.db import models
from category.models import Category


class Project(models.Model):
    """
    Project model
    Name field
    Priority field to place the project relatively to others
    Description Field

    Link field to point to a git repo or the project itself
    Image field to show the project picture

    # NOT IMPLEMENTED
    Completion filed to show whether the project is finished

    The Project model is with One to Many relationship with Category model
    """
    name = models.CharField(max_length=64)

    priority = models.IntegerField()

    description = models.CharField(max_length=256)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    link = models.CharField(max_length=512)
    image = models.ImageField(upload_to="projects/")
    is_complete = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns Capitalised name of the discipline
        so the object in the admin panel is more readable
        """
        return self.name.capitalize()
