from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length = 10)
    lastname = models.CharField(max_length = 10)
    emp_Id = models.IntegerField()

    def __str__(self):
        return self.firstName
