from django.db import models

# Create your models here.

from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=32,primary_key=True)
    memtest = models.CharField(max_length=32)
    homo_linpack = models.CharField(max_length=32)
    heter_linpack = models.CharField(max_length=32)
    heter_dgemm = models.CharField(max_length=32)
    heter_stream = models.CharField(max_length=32)

