from django.db import models
from account.models import User
from django.utils import timezone
# Create your models here.


class SubjectProfile(models.Model):
	title	= models.CharField(max_length=255)
	slug 	= models.SlugField(max_length=255, unique=True)


class StudentProfile(models.Model):
	GENDER_TYPE		= (
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Rather Not Mention')
	)
	STUDENT_CLASS = (
		('JSS1', 'Junior Secondary School 1'),
		('JSS2', 'Junior Secondary School 2'),
		('JSS3', 'Junior Secondary School 3'),
		('SS1', 'Senior Secondary School 1'),
		('SS2', 'Senior Secondary School 2'),
		('SS3', 'Senior Secondary School 3'),
	)
	user 	= models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
	first_name		= models.CharField(max_length=255, blank=True, null=True)
	other_name		= models.CharField(max_length=255, blank=True, null=True)
	last_name		= models.CharField(max_length=255, blank=True, null=True)
	photo			= models.ImageField(upload_to='media/student/images')
	qualification 	= models.FileField(upload_to='media/student/certificates')
	gender 			= models.CharField(max_length=60, choices=GENDER_TYPE)
	country			= models.CharField(max_length=255, blank=True, null=True)
	state_of_origin	= models.CharField(max_length=255, blank=True, null=True)
	residential_area= models.CharField(max_length=255, blank=True, null=True)
	zipcode 		= models.CharField(max_length=30, blank=True, null=True)
	mailing_address	= models.TextField(blank=True,null=True)
	mobile_number	= models.CharField(max_length=255, blank=True, null=True)
	student_class   = models.CharField(max_length=60,choices=STUDENT_CLASS)
	subjects 		= models.ManyToManyField(SubjectProfile)
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	date_of_birth	= models.DateField(default=timezone.now)
	date_of_joining = models.DateField(default=timezone.now)

	def get_full_name(self):
		return '{} {} {}'.format(self.first_name, self.other_name, self.last_name)

	def __str__(self):
		return self.get_full_name()

		
	
class TeacherProfile(models.Model):
	GENDER_TYPE		= (
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Rather Not Mention')
	)
	TEACHER_CLASS 	= (
		('JSS1', 'Junior Secondary School 1'),
		('JSS2', 'Junior Secondary School 2'),
		('JSS3', 'Junior Secondary School 3'),
		('SS1', 'Senior Secondary School 1'),
		('SS2', 'Senior Secondary School 2'),
		('SS3', 'Senior Secondary School 3'),
	)
	user 			= models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
	first_name		= models.CharField(max_length=255, blank=True, null=True)
	other_name		= models.CharField(max_length=255, blank=True, null=True)
	last_name		= models.CharField(max_length=255, blank=True, null=True)
	photo			= models.ImageField(upload_to='media/teacher/images')
	qualification 	= models.FileField(upload_to='media/teacher/certificates')
	gender 			= models.CharField(max_length=60, choices=GENDER_TYPE)
	nationality		= models.CharField(max_length=255, blank=True, null=True)
	state_of_origin	= models.CharField(max_length=255, blank=True, null=True)
	residential_area= models.CharField(max_length=255, blank=True, null=True)
	country			= models.CharField(max_length=255, blank=True, null=True)	
	zipcode 		= models.CharField(max_length=30, blank=True, null=True)
	teacher_class 	= models.CharField(max_length=60, choices=TEACHER_CLASS)
	subjects 		= models.ManyToManyField(SubjectProfile)
	mailing_address	= models.TextField(blank=True,null=True)
	mobile_number	= models.CharField(max_length=255, blank=True, null=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	date_of_birth	= models.DateField(default=timezone.now)
	date_of_joining = models.DateField(default=timezone.now)
	

	def get_full_name(self):
		return '{} {} {}'.format(self.first_name, self.other_name, self.last_name)

	def __str__(self):
		'''Returns the string representation of the TeacherProfile object'''
		return self.get_full_name()





