from django.db import models
from django.contrib.auth.models import User

class Graph(models.Model):

    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='calculator/saved_graphs/')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
