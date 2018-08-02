# from the inbuilt db module
from django.db import models
# timezone module
from django.utils import timezone

# from the account model
from account.models import (
	User,
)

# from the profile model
from profiles.models import (
	TeacherProfile,
)

# custom fields
from .fields import OrderField

# Content types
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Subject(models.Model):
	title	= models.CharField(max_length=255)
	slug 	= models.SlugField(max_length=255, unique=True)


	class Meta:
		ordering 	= ('title',)

	def __str__(self):
		return str(self.title)


class CourseOutline(models.Model):
	teacher 	= models.ManyToManyField(TeacherProfile)
	subject 	= models.OneToOneField(Subject, on_delete=models.CASCADE, related_name='course')
	title		= models.CharField(max_length=200)
	slug 		= models.SlugField(max_length=200,unique=True)
	overview	= models.TextField()
	created 	= models.DateTimeField(auto_now_add=True)





	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return str(self.title)

class Module(models.Model):
	course_outline 	= models.ForeignKey(CourseOutline, on_delete=models.CASCADE,related_name='modules')
	title 			= models.CharField(max_length=200)
	description 	= models.TextField(blank=True)
	order 			= OrderField(blank=True,for_fields=['course_outline'])

	class Meta:
		ordering = ['order',]


	def __str__(self):
		return "{}. {}".format(self.order, self.title)


class Content(models.Model):
	module 			= models.ForeignKey(Module, on_delete=models.CASCADE,related_name='contents')
	content_type 	= models.ForeignKey(ContentType, 
							on_delete=models.CASCADE,
							limit_choices_to={'model__in':('text',
															'video',
															'image',
															'file')})
	object_id 		= models.PositiveIntegerField()
	items 			= GenericForeignKey('content_type', 'object_id')
	order 			= OrderField(blank=True, for_fields=['module'])

	class Meta:
		ordering = ['order']


class ItemBase(models.Model):
	teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE,related_name='%(class)s_related')
	title   = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class Text(ItemBase):
	content = models.TextField()

class File(ItemBase):
	file = models.FileField(upload_to='media/content/files')

class Image(ItemBase):
	file = models.ImageField(upload_to='media/content/images')


class Video(ItemBase):
	url = models.URLField()



