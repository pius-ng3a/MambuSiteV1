from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
#from members.models import Member
# Create your models here.

class Quarter(models.Model):
	"""Quarter"""
	name=models.CharField(max_length=30)
	#leader_id= models.ForeignKey(Member,on_delete=models.CASCADE, default=1) #1 = audio, 2=video, 3=text
	description = models.CharField(max_length=250,null=True)
	population = models.IntegerField(default=200)
	area = models.CharField(max_length=100,default="600 Squared KM")
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
     
	 
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('quarter')
	  	
	def __str__(self):
		return self.name
class ProjectForm(ModelForm):
	"""docstring for ProjectForm"""
	class Meta:
		model = Quarter
		fields = ['name','area','description','population'] #'leader_id',
class AddQuarter(ModelForm):
	"""docstring for AddQuarter"""
	def __init__(self, arg):
		super(AddQuarter, self).__init__()
		self.arg = arg
		
