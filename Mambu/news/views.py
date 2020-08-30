from django.shortcuts import render
from django.http import HttpResponse
from news.models import News
from podcasts.models import Podcast
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def news(request):
	news_items = News.objects.order_by('-created_at')[2:10]
	latest_news=News.objects.order_by('-created_at')[:2]
	podcast_items = Podcast.objects.order_by('-created_at')[2:10]
	latest_podcast = Podcast.objects.order_by('-created_at')[:2]
	return render(request, "news.html",{'news_items':news_items,'podcast_items':podcast_items,'latest_news':latest_news,'latest_podcast':latest_podcast})
def contact(request):
    return render(request, "contact.html")

class PlayMovie(TemplateView):
	"""docstring for PlayMovie"""
	template_name="play.html"

def play_video(request,videoid):
	video =News.objects.get(pk = videoid)
	return render(request, 'play.html',{"video":video})
		
def save_created_movie(request):
	if request.method == "POST":
		form = MovieForm(request.POST,request.FILES)
		if form.is_valid(): #check that the form has all fields specified as needed
			form.save()
			return redirect('movie/')
		else:
			form = MovieForm()
			return render(request,'edit_movie.html',{'form':form})
def create_new_movie(request):
	form = MovieForm(request.POST,request.FILES)
	return render(request,'addmovie.html',{'form':form})

#class MovieFormView(CreateView):
#	form_class = AddMovieForm
#	template_name = 'addmovie.html'
	#success_url =''
def delete(request,movieid):
	Movie.objects.get(pk=movieid).delete()
	return redirect('movie')
def edit_movie(request,movieid):
	
	instance = Movie.objects.get(pk=movieid)
	if request.method == "POST":
		form =MovieForm(request.POST,request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			return redirect("movie")
	else:
		form = MovieForm(instance=instance)
		return render(request,'edit_movie.html',{'form':form})