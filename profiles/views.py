from django.shortcuts import render
from django.views.generic.edit  import(
 UpdateView,
 CreateView
)


from .models import (
	StudentProfile,
	TeacherProfile
)
from .forms import StudentCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here.


def dashboard(request):
	if request.user.is_authenticated:
		if request.user.student == True:
			user  = StudentProfile.objects.get(user=request.user)
		elif request.user.teacher == True:
			user  = TeacherProfile.objects.get(user=request.user)
		else:
			user = request.user
			user.first_name = 'Admin'
		print(user.first_name)	
	profile 	= 'My Dashboard'
	template_name= 'profile/dashboard.html'
	context		= {
	'dashboard':profile,
	'student_name':user.first_name,
	}
	return render(request,template_name, context)



class CreateStudentView(CreateView):
	model = StudentProfile
	form_class = StudentCreationForm
	success_url = reverse_lazy('account/profile')
	template_name = 'profile/profile_edit.html'



# @method_decorator(login_required, name='dispatch')
# class UpdateStudentProfile(UpdateView):
# 	model 	= StudentProfile
# 	fields 	= (
# 			'first_name',
# 			'other_name',
# 			'last_name',
# 			'headshot',
# 			'gender',
# 			'country',
# 			'state_of_origin',
# 			'residential_area',	
# 			'mailing_address',	
# 			'mobile_number',
# 		)
# 	template_name = 'profile_edit.html'
# 	pk_url_kwarg  = 'user_pk'
# 	context_object_name ='user'


# 	def form_valid(self, form):
# 		user = form.save(commit=False)
# 		user.updated_by = self.request.user
# 		user.updated_at = timezone.now
# 		user.save()
# 		return redirect('/account/profile', pk=user.id)
