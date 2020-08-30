from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

def get_upload_file_name(instance,filename): #function to rename files and give a unique name
	return "upld_videos/%s_%s"%(str(time()).replace('.','_'),filename)

def get_uploaded_image(instance,filename):
	return "upld_img/%s_%s"%(str(time()).replace('.','_'),filename)
class News(models.Model):
	"""movie object ot be played by users"""
	title=models.CharField(max_length=50)
	description = models.CharField(max_length=150)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
	#icon =models.ImageField(upload_to=get_uploaded_image,default="default.png",blank=True)
	video_url = models.FileField(upload_to=get_upload_file_name)
	likes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('news')
	# def __init__(self, arg):
	# 	super(Movie, self).__init__()
	# 	self.arg = arg
	# 	
	def __str__(self):
		return self.title
class NewsForm(ModelForm):
	"""docstring for NewsForm"""
	class Meta:
		model = News
		fields = ['title','description','video_url','user_id'] # ,'icon' left out, user_id should be picked from auth_user
class AddNews(ModelForm):
	"""docstring for AddNews"""
	def __init__(self, arg):
		super(AddNews, self).__init__()
		self.arg = arg
		