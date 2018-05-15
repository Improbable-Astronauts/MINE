from django.urls import path
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static 

from . import views


app_name='movies'

urlpatterns = [

    path('', views.movie_list, name='movie_list'),

]

#urlpatterns += staticfiles_urlpatterns()