from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from students.models import Student, StudentMark
from students.serializers import StudentSerializer, StudentMarkSerializer, StudentMarkFormSerializer
from rest_framework.decorators import api_view


class ListStudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudentAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UpdateStudentAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudentAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class ShowStudentAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ListStudentMarkAPIView(ListAPIView):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer


class CreateStudentMarkAPIView(CreateAPIView):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkFormSerializer


class UpdateStudentMarkAPIView(UpdateAPIView):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkFormSerializer


class DeleteStudentMarkAPIView(DestroyAPIView):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return JsonResponse({'message': 'StudentMark was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class ShowStudentMarkAPIView(RetrieveAPIView):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkFormSerializer
