from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

def get_upload_file_name(instance,filename): #function to rename files and give a unique name
	return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)
class Project(models.Model):
	"""movie object ot be played by users"""
	title=models.CharField(max_length=50 )
	budget = models.FloatField(default=100.0) #1 = audio, 2=video, 3=text
	description = models.CharField(max_length=250)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
	start_date = models.DateField(blank=True,null=True)
	end_date = models.DateField(blank=True,null=True)
	 
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('project')
	  	
	def __str__(self):
		return self.title
class ProjectForm(ModelForm):
	"""docstring for ProjectForm"""
	class Meta:
		model = Project
		fields = ['title','budget','description','start_date','end_date']
class AddProject(ModelForm):
	"""docstring for AddMovie"""
	def __init__(self, arg):
		super(AddProject, self).__init__()
		self.arg = arg
		