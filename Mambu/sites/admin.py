from django.contrib import admin
from .models import Site
# Register your models here.
 
 
class SiteAdmin(admin.ModelAdmin):
	"""docstring for SiteAdmin"""
	fieldsets=[
	("Site Name ",{'fields':['name']}),
	("Description ",{'fields':['descritption']}),
	("Picture ",{'fields':['site_image']}),
     
	 
	]
 
admin.site.register(Site)