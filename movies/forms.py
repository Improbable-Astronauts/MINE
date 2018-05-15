from django import forms

from .models import Movie

class SearchForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', )
        #widgets={'title': Textarea=(attrs={'cols': 50, 'rows': 1})}
