from django.urls import path,re_path

from . import views


app_name = 'courses'

urlpatterns = [
	re_path('^home/$',views.GreetingView.as_view(),name='greeting'),
]
