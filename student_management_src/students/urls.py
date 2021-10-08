from django.conf.urls import url
from students import views
urlpatterns = [
    url(r'^api/students$', views.student_list),
    url(r'^api/students/(?P<pk>[0-9]+)$', views.student_detail),
]