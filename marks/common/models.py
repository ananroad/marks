from django.db import models

# Create your models here.
class Userinfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    marksNum = models.IntegerField(null=False)
    createTime = models.DateTimeField(null=False)


