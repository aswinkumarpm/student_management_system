from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView

from students.models import Student, StudentMark
from students.serializers import StudentSerializer, StudentMarkSerializer, StudentMarkFormSerializer


class ListStudentAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudentAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'pk'
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "Student deleted successfully"
        },
            status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()


class ListStudentMarkAPIView(ListAPIView):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer


class CreateStudentMarkAPIView(CreateAPIView):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkFormSerializer


class StudentMarkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = StudentMark.objects.all()
    lookup_field = 'pk'
    serializer_class = StudentMarkFormSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "Student Mark deleted successfully"
        },
            status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()
