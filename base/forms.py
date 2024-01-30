from django import forms
from .models import Tournament,Request
from django.forms import ModelForm
from django.contrib.auth.models import User

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
            'start_date' : forms.DateInput(attrs={'class':'form-control my-1','placeholder':'Started date','type':'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control my-1', 'placeholder':'Ending date','type':'date'}),
            'finished' : forms.CheckboxInput(attrs={'class':'form-check','placeholder':'Finished ?'}),
            'available' : forms.CheckboxInput(attrs={'class':'form-check my-1', 'placeholder': 'Available'})
        }

class RequestForm(ModelForm):
    
    class Meta:
        model = Request
        fields = ('player', 'tournament')
    
    def __init__(self, User=None, **kwargs):
        super(RequestForm, self).__init__(**kwargs)
        if User:
            self.fields['tournament'].queryset = Tournament.objects.filter(finished=False)
    
    
class ApprovalRequestForm(ModelForm):

    class Meta:
        model = Request
        fields = ('is_approved','checked')
        labels = {
            'is_approved': 'I Approve this player to participate the Tournament',
            'checked': 'I have checked'
        }
        widgets = {
            'is_approved': forms.CheckboxInput(attrs={'class':'form-check', 'placeholder':'Approve'}),
            'checked': forms.CheckboxInput(attrs={'class':'form-check', 'placeholder':'I have checked'})
            }