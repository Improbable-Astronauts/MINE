from django import forms

from .models import Movie, Review

class SearchForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', )
        #widgets={'title': Textarea=(attrs={'cols': 50, 'rows': 1})}


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'stars', 'body',)

