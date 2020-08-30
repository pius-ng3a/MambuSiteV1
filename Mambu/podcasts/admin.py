from django.contrib import admin

from .models import Podcast
# Register your models here.
'title','description','podcast_url','user_id'
 
class PodcastAdmin(admin.ModelAdmin):
	"""docstring for SiteAdmin"""
	fieldsets=[
	("Title ",{'fields':['title']}),
	("Description ",{'fields':['descritption']}),
	("Audio ",{'fields':['podcast_url']}),
    ("User ",{'fields':['user_id']}),
     
	 
	]
 
admin.site.register(Podcast)