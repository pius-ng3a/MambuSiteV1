from django.contrib import admin

# Register your models here.

from .models import Quarter
 
class QuarterAdmin(admin.ModelAdmin):
	"""docstring for QuarterAdmin"""
    
	fieldsets=[
	("Quarter Name ",{'fields':['name']}),
	("surface Area ",{'fields':['area']}),
	("Description ",{'fields':['descritption']}),
	("Population ",{'fields':['population']}),
    ("Quarter Leader",{'fields':['leader_id']}),
	 
	]
 
admin.site.register(Quarter)