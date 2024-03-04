from django import forms
from django.forms import ModelForm
from .models import Profile,Point

class EditProfile(ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'bio','pubg_id')
        widgets = {
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control my-1','placeholder':'Profile picture'}),
            'bio':forms.Textarea(attrs={'class':'form-control my-1', 'placeholder':'Bio'}),
            'pubg_id': forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Pubg id'})
            }

class AddPointForm(ModelForm):

    class Meta:
        model = Point
        fields = ('player', 'points', 'reason')
        widgets = {
            'player' : forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Player'}),
            'points' : forms.NumberInput(attrs={'class':'form-control my-1', 'placeholder':'Point'}),
            'reason' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Reason'}),
        }


        