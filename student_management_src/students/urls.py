from django.conf.urls import url
from django.urls import path, include
from students import views
urlpatterns = [
    # url(r'^students_list$', views.student_list),
    # url(r'^student/(?P<pk>[0-9]+)$', views.student_detail),

    path("",views.ListStudentAPIView.as_view(),name="student_list"),
    path("create/", views.CreateStudentAPIView.as_view(),name="student_create"),
    path("update/<int:pk>/",views.UpdateStudentAPIView.as_view(),name="update_student"),
    path("delete/<int:pk>/",views.DeleteStudentAPIView.as_view(),name="delete_student"),



    path("marks/", views.ListStudentMarkAPIView.as_view(), name="student_marks"),
    path("marks/create/", views.CreateStudentMarkAPIView.as_view(), name="student_marks_create"),
    path("marks/update/<int:pk>/", views.UpdateStudentMarkAPIView.as_view(), name="update_student_marks"),
    path("marks/delete/<int:pk>/", views.DeleteStudentMarkAPIView.as_view(), name="delete_student_marks")
]