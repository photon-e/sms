from django.shortcuts import render
from .models import (
	StudentProfile,
	TeacherProfile
)
# Create your views here.


def dashboard(request):
	if request.user.is_authenticated:
		if request.user.student == True:
			user  = StudentProfile.objects.get(user=request.user)
		elif request.user.teacher == True:
			user  = TeacherProfile.objects.get(user=request.user)
		print(user.first_name)	
	profile 	= 'My Dashboard'
	template_name= 'profile/dashboard.html'
	context		= {
	'dashboard':profile,
	'student_name':user.first_name,
	}
	return render(request,template_name, context)