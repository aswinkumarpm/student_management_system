from django.conf.urls import url
from django.urls import path, include
from students import views

urlpatterns = [

    path("", views.ListStudentAPIView.as_view(), name="student_list"),
    path("create/", views.CreateStudentAPIView.as_view(), name="student_create"),
    path("<int:pk>/", views.StudentRetrieveUpdateDestroyView.as_view(), name="student_show"),

    path("marks/", views.ListStudentMarkAPIView.as_view(), name="student_marks"),
    path("marks/create/", views.CreateStudentMarkAPIView.as_view(), name="student_marks_create"),
    path("marks/<int:pk>/", views.StudentMarkRetrieveUpdateDestroyView.as_view(), name="student_marks_show"),
]
