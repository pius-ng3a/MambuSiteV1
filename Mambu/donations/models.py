from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from method.models import Method
# Create your models here.
class Donation(models.Model):
	"""movie object ot be played by users"""
	name=models.CharField(max_length=50 )
	amount= models.FloatField(null=False) #1 = audio, 2=video, 3=text
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
	date_donated = models.DateField(blank=True, null=True)
	method =models.ForeignKey(Method,on_delete=models.CASCADE)
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('donation')
	# def __init__(self, arg):
	# 	super(Movie, self).__init__()
	# 	self.arg = arg
	# 	
	def __str__(self):
		return self.name
class DonationForm(ModelForm):
	"""docstring for MovieForm"""
	class Meta:
		model = Donation
		fields = ['name','amount','date_donated','method']
class AddDonation(ModelForm):
	"""docstring for AddMovie"""
	def __init__(self, arg):
		super(AddDonation, self).__init__()
		self.arg = arg
