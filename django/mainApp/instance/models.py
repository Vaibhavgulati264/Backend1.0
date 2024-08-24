from django.db import models

# Create your models here.
class Instance(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=224)
    year = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
