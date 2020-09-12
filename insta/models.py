from django.db import models

# Create your models here.
class Post(models.Model):
    # title=models.CharField(max_length=100)
    caption=models.TextField()
    posts=models.ImageField(upload_to='posts/images')
    

    def __str__(self):
        return self.caption