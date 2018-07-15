from django.urls import path, re_path,include
from profiles import views as profile_view
from django.contrib.auth import views as auth_view


app_name = 'account'

urlpatterns = [
	
	re_path('^$', auth_view.LoginView.as_view(template_name='account/login.html'), name='login' ),
	re_path('^logout/$', auth_view.LogoutView.as_view(template_name='account/logout.html'), name='logout'),	
	re_path('^profile/$', profile_view.dashboard, name='profile'),
]



