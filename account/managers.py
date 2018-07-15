from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		'''
			taking all the required fields
		'''

		if not email:
			raise ValueError('Users must have an email address')

		if not password:
			raise ValueError('Users must have a password')
		user_obj = self.model(
			email = self.normalize_email(email)
		)
		user_obj.set_password(password)
		user_obj.save(using=self._db)
		return user_obj


	

	def create_superuser(self, email, password=None):
		user 	= self.create_user(
				email,
				password=password,
		)
		user.admin = True
		user.save(using=self._db)
		return user

