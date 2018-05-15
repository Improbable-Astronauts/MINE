from django.test import TestCase

from .models import Movie 



class MovieModelTests(TestCase):
    def setUp(self):

        Movie.objects.create(title="The Shining", year="1980", length="146 min")
        Movie.objects.create(title="Dead Men Don't Wear Plaid", year="1982", length="too long")
        Movie.object.create(title="laskdfjlaskjf", year="hamburger", length="17hours")
        Movie.object.create(title="The White Horse", year="1967", lenght='')

    def test_lenght_to_hours(self):
        pass

        
