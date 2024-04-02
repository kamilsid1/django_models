from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.IntegerField()
    Add = models.CharField(max_length=100)
    City = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ["-Name"]  
        # this is used for ordering data in ascending and descending 
        
        verbose_name = "stu"
        # this is used to change name of the table
        
        verbose_name_plural = "stu"
        # As "s" comes by default, so to remove it we use this code 

        db_table = "stu_table"
        # To change the table name in db sqlite
