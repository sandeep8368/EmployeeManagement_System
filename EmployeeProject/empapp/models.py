from django.db import models

# Create your models here.
class empModel(models.Model):
    name = models.CharField(max_length=40)
    addr = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    phome = models.IntegerField()
    