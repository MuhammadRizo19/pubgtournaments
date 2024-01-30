from django import forms
from django.forms import ModelForm
from .models import Profile

class EditProfile(ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'bio','pubg_id')
        widgets = {
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control my-1','placeholder':'Profile picture'}),
            'bio':forms.Textarea(attrs={'class':'form-control my-1', 'placeholder':'Bio'}),
            'pubg_id': forms.TextInput(attrs={'class':'form-control my-1','placeholder':'Pubg id'})
            }