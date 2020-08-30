from django.contrib import admin
from .models import News

# Register your models here.
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	"""docstring for MemberAdmin"""
	fieldsets=[
	("Title ",{'fields':['title']}),
	("Description ",{'fields':['descritption']}),
	("Video ",{'fields':['video_url']}),
    ("User Id ",{'fields':['user_id']}),
	 
	]
 
admin.site.register(News)