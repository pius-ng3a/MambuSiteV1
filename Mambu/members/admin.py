from django.contrib import admin
from .models import Member

# Register your models here.
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
	"""docstring for MemberAdmin"""
	fieldsets=[
	("First name",{'fields':['Fname']}),
	("Last name ",{'fields':['Lname']}),
	("Email: ",{'fields':['email']}),
	("Quarter in Mambu ",{'fields':['quarter']}),
	 
	]
 
admin.site.register(Member)