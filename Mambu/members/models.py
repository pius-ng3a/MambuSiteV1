from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from quarters.models import Quarter

# Create your models here.
class Member(models.Model):
	"""movie object ot be played by users"""
	Fname=models.CharField(max_length=15)
	Lname=models.CharField(max_length=25)
	quarter = models.ForeignKey(Quarter,default=1,on_delete=models.CASCADE)
	email= models.EmailField(max_length=254,null=True) #Some people will not have email addresses
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
	def __unicode__(self):
		return self.Lname +" "+ self.Fname
	def get_absolute_url(self):
		return reverse('member')
	# def __init__(self, arg):
	# 	super(Movie, self).__init__()
	# 	self.arg = arg
	# 	
	def __str__(self):
		return self.Lname +" " +self.Fname
class MemberForm(ModelForm):
	"""docstring for MovieForm"""
	class Meta:
		model = Member
		fields = ['Fname','Lname','email','quarter']
class AddMember(ModelForm):
	"""docstring for AddMovie"""
	def __init__(self, arg):
		super(AddMember, self).__init__()
		self.arg = arg
