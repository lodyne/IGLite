from django.db import models

# Create your models here.
class Post(models.Model):
    caption=models.TextField()
    posts=models.ImageField(upload_to='posts/images')
    

    def __str__(self):
        return self.caption