from django.contrib import admin

from .models import Project

# Register your models here.
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	"""docstring for ProjectAdmin"""
	fieldsets=[
	("Title ",{'fields':['title']}),
	("Budget ",{'fields':['budget']}),
	("Description ",{'fields':['descritption']}),
	("Start Date ",{'fields':['start_date']}),
    ("end_date",{'fields':['end_date']}),
	 
	]
 
admin.site.register(Project)