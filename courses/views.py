# from braces.views import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic import (
# 		ListView,
# 		DetailView,
# 		CreateView,
# 		DeleteView,
# 		UpdateView
# 		)
# from .models import Course
# # Create your views here.


# class OwnerMixin(object):
# 	def get_queryset(self):
# 		qs 	=super(OwnerMixin, self).get_queryset()
# 		return qs.filter(owner=self.request.user)


# class OwnerEditMixin(Object):
# 	def form_valid(self, form):
# 		form.instance.owner = self.request.user
# 		return super(OwnerEditMixin, self).form_valid(form)


# class OwnerCourseMixin(OwnerMixin):
# 	model 	= Course
# 	fields	= ['subject', 'title', 'slug', 'overview']
# 	success_url	= reverse_lazy('manage_course_list')



# class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
# 	fields 	= ['subject', 'title','slug', 'overview']
# 	success_url	= reverse_lazy('manage_course_list')
# 	template_name 	=	'courses/manage/course/form.html'

	

# class ManageCourseListView(OwnerCourseMixin,ListView):
# 	template_name	= "courses/manage/courses/list.html"

# class CourseCreateView(PermissionRequiredMixin,OwnerCourseEditMixin, CreateView):
# 	permission_required 	= 'courses.add_course'


# class CourseUpdateView(PermissionRequiredMixin,OwnerCourseEditMixin, UpdateView):
# 	permission_required 	= 'courses.chanage_course'

# class CourseDeleteView(PermissionRequiredMixin,OwnerCourseEditMixin, DeleteView):
# 	template_name 	= 'courses/manage/courses/delete.html'
# 	success_url 	= reverse_lazy('manage_course_list')
# 	permission_required 	=  'courses.delete_course'




