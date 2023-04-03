from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name
