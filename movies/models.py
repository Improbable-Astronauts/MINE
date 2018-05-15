from django.db import models

from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=500)
    year = models.CharField(max_length=4)
    length = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_length_in_hours(self):
        ints_in_length = [char for char in self.length if char is int]
        minutes = int(''.join(ints_in_length))
        hours = minutes//60
        and_minutes = minutes % 60
        
        return "{} hours and {} minutes".format(hours, and_minutes)
