from django.db import models

# Create your models here.
class Experiences(models.Model):
    date = models.CharField(max_length=200)
    position = models.CharField(max_length =200)
    company = models.CharField(max_length =200)
    description = models.TextField()

    def __str__(self):
        return self.date

class Contact(models.Model):
    name = models.CharField(max_length = 300)
    email = models.EmailField(max_length = 100)
    message = models.TextField()


    def __str__(self):
        return self.name
