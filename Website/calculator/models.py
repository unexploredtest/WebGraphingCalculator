from django.db import models
from django.contrib.auth.models import User

class Graph(models.Model):

    equation = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
