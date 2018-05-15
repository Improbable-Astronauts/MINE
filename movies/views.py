from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import omdb

from .models import Movie
from .forms import SearchForm


# Create your views here.

def movie_list(request):
    ''' diplays list of movies as main body (search on side)'''

    movies = Movie.objects.all().order_by('title')
    # paginations if to show only five movies per page
    paginator = Paginator(movies, 5)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    
    if request.method == "POST":
       
        form = SearchForm(request.POST)
        msg = None
       


        if form.is_valid():
            movie = form.save(commit=False)

            details = omdb.get(title=movie.title)

            if details:
                movie.year = details['year']
                movie.length = details['runtime']
                try:
                    movie.save()
                    messages.add_message(request, messages.SUCCESS, "Movie added")
                    print("movie saved to db")
                except:
                    messages.add_message(request, messages.INFO, "Unable to save")
                    print("not saved")
            else:
                msg = "Movie not found, maybe you can't spell for doo-doo."
        movies = Movie.objects.all().order_by('title')
        return render(request, 'movies/list.html', {'movies':movies, 'form':form, 'msg':msg, 'page':page,})

    else:
        form = SearchForm()
        
        return render(request, 'movies/list.html', {'movies':movies, 'form':form, 'page':page,})
