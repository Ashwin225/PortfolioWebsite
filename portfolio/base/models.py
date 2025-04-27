from django.db import models

# Create your models here.

class ContactMe(models.Model):
    name = models.CharField(max_length=225)
    email= models.EmailField(max_length=40)
    content=models.TextField(max_length=400)
    number=models.CharField(max_length=10)

    def __str__(self):
        return self.name
