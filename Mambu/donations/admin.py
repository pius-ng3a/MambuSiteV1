from django.contrib import admin

from .models import Donation
# Register your models here.
fields = ['name','amount','date_donated','method']
class DonationAdmin(admin.ModelAdmin):
	"""docstring for DonationAdmin"""
	fieldsets=[
	("Donor Name",{'fields':['name']}),
	("Amount ",{'fields':['amount']}),
	("Date donated: ",{'fields':['date_donated']}),
	("Method ",{'fields':['method']}),
	
	]
 
admin.site.register(Donation)
#admin.site.site_header = "Aministration 