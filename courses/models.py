from django.db import models
from account.models import User


class Subject(models.Model):
	title	= models.CharField(max_length=255)
	slug 	= models.SlugField(max_length=255, unique=True)


	class Meta:
		ordering 	= ('title',)

	def __str__(self):
		return str(self.title)


# from django.db import models
# from .fields import OrderField
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey

# # Create your models here.
# # from django.contrib.auth.models import User
# from account.models import MyUser


# class Subject(models.Model):
# 	title  = models.CharField(max_length=200)
# 	slug   = models.CharField(max_length=300, unique=True)

# 	class Meta:
# 		ordering = ('title',)


# 	def __str__(self):
# 		return str(self.title)



# class Course(models.Model):
# 	owner 		= models.ForeignKey(MyUser, related_name='course_created', on_delete='models.CASCADE')
# 	subject 	= models.ForeignKey(Subject, related_name='courses', on_delete='models.CASCADE') # ont to one relationship with the Subject table
# 	title  		= models.CharField(max_length=200)
# 	slug  		= models.SlugField(max_length=300, unique=True)
# 	overview	= models.TextField()
# 	created 	= models.DateTimeField(auto_now_add=True)


# 	class Meta:
# 		ordering	= ('title',)

# 	def __str__(self):
# 		return str(self.title)

# class Module(models.Model):
# 	course 		= models.ForeignKey(Course, related_name='modules', on_delete='models.CASCADE')
# 	title 		= models.CharField(max_length=200)
# 	description = models.TextField()
# 	order 		= OrderField(blank=True, for_fields=['course'])


# 	class Meta:
# 		ordering = ['order']

# 	def __str__(self):
# 		return '{}. {}'.format(self.order, self.title)

# class ItemBase(models.Model):
# 	owner 	= models.ForeignKey(MyUser, related_name='%(class)s_related', on_delete='models.CASCADE')
# 	title 	= models.CharField(max_length=200)
# 	created = models.DateTimeField(auto_now_add=True)
# 	updated = models.DateTimeField(auto_now=True)


# 	class Meta:
# 		abstract = True

# 	def __str__(self):
# 		return str(self.title)

# class Text(ItemBase):
# 	content 	= models.TextField()


# class File(ItemBase):
# 	file 		= models.FileField(upload_to='files')

# class Image(ItemBase):
# 	file 		= models.ImageField(upload_to='images')

# class Video(ItemBase):
# 	url 		= models.URLField()

# class Content(models.Model):
# 	module 			= models.ForeignKey(Module, related_name='contents', on_delete='models.CASCADE')
# 	content_type 	= models.ForeignKey(ContentType,on_delete='models.CASCADE')
# 	object_id		= models.PositiveIntegerField()
# 	item 			= GenericForeignKey('content_type', 'object_id')
# 	content_type	= models.ForeignKey(ContentType, limit_choices_to={'model__in':(
# 																			'text',
# 																			'video',
# 																			'image',
# 																			'file'
# 																			)}, on_delete='models.CASCADE')
# 	order 			= OrderField(blank=True, for_fields=['module'])

# 	class Meta:
# 		ordering = ['order']