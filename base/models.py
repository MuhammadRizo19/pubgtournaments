from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date

class Tournament(models.Model):
   
   WEAPON = {
       'M416':'M416',
       'M24':'M24'
   }

   SQUAD = {
       'Solo':'Solo',
       'Duo':'Duo',
       'Squad':'Squad'
   }

   id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
   tournament_name = models.CharField(max_length=50)
   tournament_rules = models.TextField()
   participants = models.IntegerField()
   squad = models.CharField(max_length=30, choices=SQUAD)
   weapon = models.CharField(max_length=50, choices=WEAPON)
   started = models.BooleanField(blank=True,null=True)
   start_date = models.DateField(blank=True,null=True)
   end_date = models.DateField(blank=True,null=True)
   finished = models.BooleanField(blank=True,null=True)
   available = models.BooleanField()

   """""   
   def save(self, *args, **kwargs):
       if self.end_date < date.today():
           self.finished = True
       else:
           self.finished = False 
       super().save(*args, **kwargs)
   """""

   def __str__(self):
       return self.tournament_name

class Participant(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    participant_title = models.CharField(max_length=50)
    participant_list = models.ManyToManyField(User, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    is_open = models.BooleanField()

    def __str__(self):
        return self.participant_title 
    
class Request(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE) 
    is_approved = models.BooleanField(default=False, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    checked = models.BooleanField()
    
    def save(self, *args, **kwargs):
        if self.is_approved == True or False:
            self.checked = True
        else:
            self.checked = False
        super().save(*args, **kwargs)

#    def __str__(self):
#       return self.tournament


class Round(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    round_number = models.CharField(max_length=35)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    current = models.BooleanField(blank=True,null=True)
    date = models.DateField(auto_now_add=True, blank=True,null=True)
    
    class Meta:
        ordering = ["-date"]
    
    def __str__(self):
        return self.round_number

class Match(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    match_name = models.CharField(max_length=35)
    player_1 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = 'player1')
    player_2 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = 'player2')
    forround = models.ForeignKey(Round, on_delete=models.DO_NOTHING)
    first_match = models.CharField(max_length=35, blank=True, null=True)
    second_match = models.CharField(max_length=35, blank=True, null=True)
    third_match = models.CharField(max_length=35, blank=True, null=True)
    total = models.CharField(max_length=35, blank=True, null=True)

    def __str__(self):
        return self.match_name















"""""
class Round(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    round_name = models.CharField(max_length=50)
    tournament = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.round_name

class Match(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    match_name = models.CharField(max_length=50)
    round_number = models.ForeignKey(Round, on_delete=models.CASCADE)
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2')
    

    def __str__(self):
        return self.match_name
    

class apply(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)
    approved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

"""""        