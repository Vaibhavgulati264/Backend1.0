from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=224)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=100)