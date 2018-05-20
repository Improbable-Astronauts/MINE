from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

import omdb

from .models import Movie
from .forms import SearchForm, ReviewForm, EmailReviewForm 


# Create your views here.

def home(request):
    ''' just returns to the main movie list '''
    return movie_list(request)
    #return render(request, 'movies/list.html', {'movies':movies, 'form':form, 'page':page,})


def movie_list(request):
    ''' diplays list of movies as main body (search on side)'''

    try:
        movies = Movie.objects.all().order_by('title')
    
    #if movies:
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
    except None:
        form = SearchForm()
        return render(request, 'movies/list.html', {'form':form})

def movie_detail(request, title, year):
    # if someone just types in an url that doesn't work return404 not break
    movie = get_object_or_404(Movie, title=title, year=year)
    # list of comments about the movie
    reviews = movie.reviews.filter(active=True)

    if request.method == 'POST':
        # someone fills out a review form
        rv_form = ReviewForm(data=request.POST)

        if rv_form.is_valid():
            # everythin is legit but we don't save to db yet
            new_review = rv_form.save(commit=False)
            new_review.movie = movie
            #now that the review is assigned to the current movie save to db
            new_review.save()
    else:
        rv_form = ReviewForm()

    return render(request, 'movies/movie_detail.html', {'movie':movie, 'reviews':reviews, 'rv_form':rv_form})
    
def share_reviews(request, movie_id):#, title, year):
    # get the review you want to share
    movie = get_object_or_404(Movie, id=movie_id)
    # hasn't been mailed yet
    sent = False

    if request.method == "POST":
        mail_form = EmailReviewForm(request.POST)
        if mail_form.is_valid():
            contents = mail_form.cleaned_data # dict of form values
            movie_url = request.build_absolute_uri(movie.get_absolute_url())
            subject = '{} ({}) recommends you see "{}"'.format(contents['name'], contents['email'], movie.title)
            message = 'Read "{}" at {}\n\n{}\'s comments'.format(movie.title, movie_url, contents['name'], contents['comments'])
            send_mail(subject, message, 'jasonr.jones14@gmail.com', [contents['to']])
            sent = True 

    else:
        mail_form = EmailReviewForm()
    
    return render(request, 'movies/share.html', {'movie':movie, 'email_form':mail_form, 'sent':sent})