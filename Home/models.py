from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length = 255)
    content= models.CharField(max_length = 500)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user')