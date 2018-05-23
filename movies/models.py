from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from .starfield import StarRangeField

class Movie(models.Model):
    title = models.CharField(max_length=500)
    year = models.CharField(max_length=4)
    length = models.CharField(max_length=20)

    tags = TaggableManager() # https://django-taggit.readthedocs.io/en/latest/
    
    # class Meta:
    #     ordering = ('title',)

    def __str__(self):
        return self.title

    def get_length_in_hours(self):
        ints_in_length = [char for char in self.length if char is int]
        minutes = int(''.join(ints_in_length))
        hours = minutes//60
        and_minutes = minutes % 60
        
        return "{} hours and {} minutes".format(hours, and_minutes)

    def get_absolute_url(self):
        ''' returns the correct path for specific movie '''
        return reverse('movies:movie_detail', args=[self.title, self.year])


# had to create a custom class for integer range 1-5 for our stars
# https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model



class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    stars = StarRangeField(min_value=1, max_value=5)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # in case we want to change our review later
    updated = models.DateTimeField(auto_now=True)
    # can switch to False if Reviewer leaves 
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', ) # we could also order by weighted friends?

    def __str__(self):
        return 'Review by {} on {}'.format(self.name, self.created)