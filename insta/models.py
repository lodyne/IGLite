from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    caption = models.TextField()
    posts = models.ImageField(upload_to='posts/images')
    instagrammer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=True, default=None)

    def __str__(self):
        return self.caption

    ''' The function below tells the view where to redirect after post is
        created i.e. finds the url of the model object that returns the path
        to any specific instance (find the location to a specific post).
    '''

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


# DIFFERENCE BETWEEN REDIRECT AND REVERSE FUNCTIONS

''' Redirect function is simply to redirect you to a specific route.
                            WHILE
    Reverse function is simply return the full url to 'that' route
    as a string.
'''
