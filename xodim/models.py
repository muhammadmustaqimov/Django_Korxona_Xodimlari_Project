from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    img = models.ImageField(upload_to='images/', blank=True)
    fullname = models.CharField(max_length=200,)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    position = models.CharField(max_length=200,)
    about = models.TextField(default='Xodim :   ')

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])