from django.db import models

# Create your models here.
from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from donations.models import Donation

class Detail(models.Model):
	"""movie object ot be played by users"""
	credential= models.CharField(max_length=256 ) #encrypted for security.
	cvs = models.CharField(max_length=5) #three digit number for card. 
	donation_id = models.ForeignKey(Donation,on_delete=models.CASCADE) #links this to the donation
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
	issued_on = models.DateField(blank=True,null=True)
	expires_on = models.DateField(blank=True,null=True) #date card expires if it's a card
	def __unicode__(self):
		return self.cvs
	def __str__(self):
		return self.cvs
class DetailForm(ModelForm):
	"""docstring for MovieForm"""
	class Meta:
		model = Detail
		fields = ['credential','cvs','issued_on','expires_on','donation_id']
class AddDetail(ModelForm):
	"""docstring for AddMovie"""
	def __init__(self, arg):
		super(AddDetail, self).__init__()
		self.arg = arg
		