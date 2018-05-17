from django.urls import path
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static 

from . import views


app_name='movies'

urlpatterns = [

    path('', views.movie_list, name='movie_list'),
    path('home', views.home, name='home'),
    path('<str:title>/<int:year>', views.movie_detail, name='movie_detail'),
]

#urlpatterns += staticfiles_urlpatterns()