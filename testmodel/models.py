from django.db import models

# Create your models here.

from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    memtest = models.CharField(max_length=32, default='0')   # test column default value is 0
    homo_linpack = models.CharField(max_length=32, default='0')
    heter_linpack = models.CharField(max_length=32, default='0')
    heter_dgemm = models.CharField(max_length=32, default='0')
    heter_stream = models.CharField(max_length=32, default='0')
    change_time = models.DateTimeField(auto_now=True)
    cab = models.CharField(max_length=32)


