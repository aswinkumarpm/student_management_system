from rest_framework import serializers

from .models import Student, StudentMark


class StudentSerializer(serializers.ModelSerializer):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    TEACHER_CHOICES = (
        ('Katie', 'Katie'),
        ('Max', 'Max'),
    )
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    reporting_teacher = serializers.ChoiceField(choices=TEACHER_CHOICES)

    class Meta:
        model = Student
        fields = ('id',
                  'name',
                  'age',
                  'gender',
                  'reporting_teacher')


class StudentMarkSerializer(serializers.ModelSerializer):
    TERM_CHOICES = (
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
    )
    term = serializers.ChoiceField(choices=TERM_CHOICES)
    name = serializers.CharField(source='student.name', read_only=True)

    class Meta:
        model = StudentMark
        fields = ('id',
            'name',
                  'term',
                  'maths_mark',
                  'science_mark',
                  'history_mark',
                  'total_mark',
                  'created'

                  )

class StudentMarkFormSerializer(serializers.ModelSerializer):
    TERM_CHOICES = (
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
    )
    term = serializers.ChoiceField(choices=TERM_CHOICES)

    class Meta:
        model = StudentMark
        fields = (
                  'student',
                  'term',
                  'maths_mark',
                  'science_mark',
                  'history_mark',
                  )