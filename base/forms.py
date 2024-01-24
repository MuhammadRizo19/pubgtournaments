from django import forms
from .models import Tournament
from django.forms import ModelForm

class EditTournamentForm(ModelForm):
    
    class Meta:
        model = Tournament
        fields = (
            'tournament_name',
            'tournament_rules',
            'participants',
            'squad',
            'weapon',
            'started',
            'start_date',
            'end_date',
            'finished',
            'available'
        )
        widgets = {
            'tournament_name':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Tournament Name'}),
            'tournament_rules': forms.Textarea(attrs={'class':'form-control my-1', 'placeholder':'Tournament Rules', 'column':3}),
            'participants' : forms.NumberInput(attrs={'class':'form-control my-1', 'placeholder':'Participants amount'}),
            'squad' : forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Squad type'}),
            'weapon' : forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Weapon type'}),
            'started' : forms.CheckboxInput(attrs={'class':'form-check my-1','placeholder':'Started ?'}),
            'start_date' : forms.DateInput(attrs={'class':'form-control my-1','placeholder':'Started date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control my-1', 'placeholder':'Ending date'}),
            'finished' : forms.CheckboxInput(attrs={'class':'form-check my-1','placeholder':'Finished ?'}),
            'available' : forms.CheckboxInput(attrs={'class':'form-check my-1', 'placeholder': 'Available'})
        }