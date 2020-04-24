from django.db import models 
import re 
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 


class Document(models.Model):
    title = models.CharField(max_length=45, default="Title")
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')





