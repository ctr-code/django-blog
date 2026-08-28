from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Stores the single about message and image.
    """
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    # The about message is a singleton
    def __str__(self):
        return "About Page Content"


class CollaborationRequest(models.Model):
    """
    Stores a single collaboration request.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
