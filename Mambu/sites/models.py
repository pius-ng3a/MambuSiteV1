from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from members.models import Member
# Create your models here.

class Site(models.Model):
	"""Sites for tourism"""
	name=models.CharField(max_length=30)
	description = models.CharField(max_length=250,null=True)
	site_image = models.CharField(max_length=250,default="")
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
     
	 
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('site')
	  	
	def __str__(self):
		return self.name
class SiteForm(ModelForm):
	"""docstring for SiteForm"""
	class Meta:
		model = Site
		fields = ['name' ,'description','site_image']
class AddSite(ModelForm):
	"""docstring for AddSite"""
	def __init__(self, arg):
		super(AddSite, self).__init__()
		self.arg = arg
		
