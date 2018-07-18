from django.urls import re_path
from . import views
app_name = 'profile'

urlpatterns = [
	re_path('^$', views.CreateStudentView.as_view(), name='create'),

	# re_path('^user/(?P<pk>\d+)/$', views.UpdateStudentProfile.as_view() ,name='edit_user')
]