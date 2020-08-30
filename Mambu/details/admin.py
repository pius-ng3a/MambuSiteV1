from django.contrib import admin
from .models import Detail
# Register your models here.
class DetailAdmin(admin.ModelAdmin):
	"""docstring for DetailAdmin"""
	fieldsets=[
	("Card No or Method Name",{'fields':['credential']}),
	("CVV ",{'fields':['cvs']}),
	("Issued on: ",{'fields':['issued_on']}),
	("Expires on: ",{'fields':['expires_on']}),
	("Donation Id ",{'fields':['donation_id']}),
	]
 
admin.site.register(Detail)
#admin.site.site_header = "Aministration Dashboard" # this changes the default title

