from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',
                              height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f'{self.user.username} Profile'
