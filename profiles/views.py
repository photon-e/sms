from django.shortcuts import render
from .models import (
	StudentProfile,
	TeacherProfile
)
# Create your views here.


def dashboard(request):
	student_obj 	= StudentProfile.objects.all()
	profile 	= 'My Dashboard'
	template_name= 'profile/dashboard.html'
	context		= {
	'dashboard':profile,
	'student_user':student_obj,
	}
	return render(request,template_name, context)