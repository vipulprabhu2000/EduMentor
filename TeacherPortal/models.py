from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=250)
    Subject=models.CharField(max_length=250)
    Marks=models.CharField(max_length=20)

    def __str__(self):
        return f"{str(self.Name)}"


    
