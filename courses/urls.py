from django.urls import path,re_path

from . import views


app_name = 'courses'

urlpatterns = [
	re_path('^mine/$', views.ManageCourseListView.as_view(), name='manage_course_list'),
	re_path('^create/$', views.CourseCreateView.as_view(), name='course_create'),
	re_path('^(?P<pk>\d+)/edit/$', views.CourseUpdateView.as_view(), name='course_edit'),
	re_path('^(?P<pk>\d+)/delete/$', views.CourseDeleteView.as_view(), name='course_delete'),
	re_path('^(?P<pk>\d+)/module/$', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
]


