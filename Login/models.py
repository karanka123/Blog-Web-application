from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.\

class blog(models.Model):
    Author = models.CharField(max_length = 24)
    Title = models.CharField(max_length = 255)
    Content= models.CharField(max_length = 500)
    Image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'post_set')

    def __str__(self):
        return self.Author, self.Title
    
