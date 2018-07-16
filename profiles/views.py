from django.shortcuts import render
from .models import (
	StudentProfile,
	TeacherProfile
)
# Create your views here.


def dashboard(request):
	if request.user.is_authenticated:
		student  = StudentProfile.objects.get(user=request.user)
		print(student.first_name)	
	profile 	= 'My Dashboard'
	template_name= 'profile/dashboard.html'
	context		= {
	'dashboard':profile,
	'student_name':student.first_name,
	}
	return render(request,template_name, context)