from django.db import models

# Create your models here.
class Marks(models.Model):
    title = models.CharField(max_length = 200)
    url = models.CharField(max_length=200)
    markImg = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    belongTo = models.IntegerField(null=True,blank=True)
    remark = models.CharField(max_length=500)
    clickNum = models.CharField(max_length=10)
    createTime =models.DateTimeField(null=True,blank=True)
    
    
class Tags(models.Model):
    tagName = models.CharField(max_length=200)
    marksNum =  models.IntegerField(null=False)
    