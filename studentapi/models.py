from django.db import models

# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=3)
    city = models.CharField(max_length=15)
    school = models.CharField(max_length=30)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE