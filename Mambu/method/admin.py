from django.contrib import admin
from .models import Method

 
# Register your models here.
class MethodAdmin(admin.ModelAdmin):
	"""docstring for MemberAdmin"""
	fieldsets=[
	("Pyment Method",{'fields':['name']}),
	 
	]
 
admin.site.register(Method)