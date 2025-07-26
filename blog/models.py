from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="media/images/", null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["date_posted"]

        def __str__(self):
            return self.title
