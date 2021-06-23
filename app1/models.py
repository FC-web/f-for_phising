from django.db import models

class info(models.Model):
    ui= models.CharField(max_length=32)
    password= models.CharField(max_length=32)

