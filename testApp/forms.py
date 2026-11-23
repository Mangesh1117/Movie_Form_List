from django import forms

from .models import Movie

class MovieForm(forms.ModelForm):
    name = forms.CharField(max_length=15)
    genre = forms.CharField(max_length=10)
    director = forms.CharField(max_length=20)
    actor = forms.CharField(max_length=20)
    actress = forms.CharField(max_length=20)
    rdate = forms.DateField()
    language = forms.CharField(max_length=10)
    rating = forms.ChoiceField(choices=[("A","Adults Only"),("U","Universal"),("UA","Parental Guidance"),("S","Specialized Audience")],widget=forms.RadioSelect)

    class Meta:
        model = Movie
        fields = "__all__"