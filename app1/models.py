from django.db import models

class info(models.Model):
    ui= models.CharField(max_length=18)
    password= models.CharField(max_length=18)

