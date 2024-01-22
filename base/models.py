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
   start_date = models.DateField(blank=True,null=True)
   finished = models.BooleanField(blank=True,null=True)
   available = models.BooleanField()

   def save(self, *args, **kwargs):
       if self.start_date < date.today():
           self.finished = True
           if self.finished == True:
               self.available = False
       else:
           self.finished = False
           if self.finished == False:
               self.available = True
       super().save(*args, **kwargs)

   def __str__(self):
       return self.tournament_name

class Round(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    round_name = models.CharField(max_length=50)
    tournament = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.round_name

class Match(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
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