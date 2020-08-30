from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.
 

def get_uploaded_podcast(instance,filename):
	return "upld_pod/%s_%s"%(str(time()).replace('.','_'),filename)
class Podcast(models.Model):
    """movie object ot be played by users"""
    title=models.CharField(max_length=50)
    podcast_url = models.FileField(upload_to=get_uploaded_podcast)
    description = models.CharField(max_length=150)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
    updated_at= models.DateField(blank=True, null=True,auto_now=True)
    likes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('podcasts')
	# def __init__(self, arg):
	# 	super(Movie, self).__init__()
	# 	self.arg = arg
	# 	
    def __str__(self):
	    return self.title
class PodcastForm(ModelForm):
	"""docstring for PodcastForm"""
	class Meta:
		model = Podcast
		fields = ['title','description','podcast_url','user_id'] 
class AddPodcast(ModelForm):
	"""docstring for AddMovie"""
	def __init__(self, arg):
		super(AddPodcast, self).__init__()
		self.arg = arg
		