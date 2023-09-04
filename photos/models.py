from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=100)

    def __str__(self):
            return self.name
        

class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    category = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    image = models.ImageField(upload_to='myimage/')
    description = models.TextField()

    def __str__(self):
            return self.description