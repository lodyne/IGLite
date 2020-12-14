from PIL import Image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile.jpg',
                              height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length=50, default='DEFAULT VALUE')
    website = models.URLField(max_length=50, default='DEFAULT VALUE')
    bio = models.TextField(max_length=500, default='DEFAULT VALUE')

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, default='DEFAULT VALUE')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
