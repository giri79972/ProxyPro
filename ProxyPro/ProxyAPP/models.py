from _weakref import proxy

# Create your models here.
from django.db import models

class Emp(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=20)
    sal=models.IntegerField()
    def __str__(self):
        return self.ename
class EmpProxy(Emp):
    class Meta:
        proxy=True