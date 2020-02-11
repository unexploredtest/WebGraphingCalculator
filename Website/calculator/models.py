from django.db import models
from django.contrib.auth.models import User

class Graph(models.Model):

    equation = models.CharField(max_length=30, primary_key=True)
    description = models.TextField()
    image = models.ImageField(upload_to='graphs/')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
