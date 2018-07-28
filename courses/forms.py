from django import forms
from django.forms.models import inlineformset_factory
from .models import CourseOutline, Module




ModuleFormSet = inlineformset_factory(
		CourseOutline,
		Module,
		fields=['title', 'description'],
		extra = 2,
		can_delete=True
)