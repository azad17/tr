from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    def __str__(self):
        return self.name

class Team(models.Model):
    person = models.CharField(max_length=100)
    dp = models.ImageField(upload_to='pics')
    details = models.TextField(max_length=100)
    def __str__(self):
        return self.person