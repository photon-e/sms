from django.db import models
from django.utils import timezone
from django.contrib.auth.models import(
 	AbstractBaseUser,
 )
from .managers import UserManager


GENDER_TYPE		= (
			('M', 'Male'),
			('F', 'Female'),
			('O', 'Rather Not Mention')
	)
class User(AbstractBaseUser):
	email 			= models.EmailField(max_length=255,unique=True) # email field
	timestamp 		= models.DateTimeField(auto_now=True)
	updated 		= models.DateTimeField(auto_now_add=True)
	active 			= models.BooleanField(default=True)
	admin			= models.BooleanField(default=False)
	teacher			= models.BooleanField(default=False)
	student			= models.BooleanField(default=False)


	objects 		= UserManager()





	USERNAME_FIELD = 'email'   # email as auth_token
	REQUIRED_FIELDS = []


	def __str__(self):
		return str(self.email)


	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.admin



