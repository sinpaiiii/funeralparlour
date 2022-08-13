from django.db import models

class startUp(models.Model):
    # id field is added automatically
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    startUpName = models.CharField(max_length=40)
    desc = models.TextField()
    funds = models.BooleanField()
    contactNumber = models.IntegerField()
    email = models.BooleanField()
    # images= models.ImageField(upload_to ="images")
