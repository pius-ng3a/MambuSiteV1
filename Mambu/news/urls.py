from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
] 