from django.db import models

# Create your models here.
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
 

class Method(models.Model):
	"""movie object ot be played by users"""
	name=models.CharField(max_length=25 )
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('method')
	# def __init__(self, arg):
	# 	super(Movie, self).__init__()
	# 	self.arg = arg
	# 	
	def __str__(self):
		return self.name
class MethodForm(ModelForm):
	"""docstring for MethodForm"""
	class Meta:
		model = Method
		fields = ['name']
class AddMethod(ModelForm):
	"""docstring for AddMethod"""
	def __init__(self, arg):
		super(AddMethod, self).__init__()
		self.arg = arg

