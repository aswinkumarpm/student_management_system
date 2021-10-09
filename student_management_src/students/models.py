from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    reporting_teacher = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class StudentMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(max_length=50)
    maths_mark = models.IntegerField()
    science_mark = models.IntegerField()
    history_mark = models.IntegerField()
    total_mark = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.name


    def save(self, *args, **kwargs):
        self.total_mark = int(self.history_mark) + int(self.science_mark)+ int(self.maths_mark)
        super(StudentMark, self).save(*args, **kwargs)

#Reporting Teacher - It should be a selectable list.

#StudentMarks

#student forignkey
#term_selction choice one, two
#subject
# Subject -
# Maths -> Marks
# Science -> Marks
# History -> Marks