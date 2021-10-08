from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    reporting_teacher = models.CharField(max_length=50)
#Reporting Teacher - It should be a selectable list.

#StudentMarks

#student forignkey
#term_selction choice one, two
#subject
# Subject -
# Maths -> Marks
# Science -> Marks
# History -> Marks