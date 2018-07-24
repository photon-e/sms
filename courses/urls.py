from django.urls import path,re_path

from . import views


app_name = 'courses'

urlpatterns = [
	re_path('^mine/$', views.ManageCourseListView.as_view(), name='manage_course_list'),
	re_path('^create/$', views.CourseCreateView.as_view(), name='course_create'),

]
