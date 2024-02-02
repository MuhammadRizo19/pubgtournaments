from collections.abc import Iterable
from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images/', default='default/default.jpg', blank=True, null=True)
    bio = models.TextField(blank=True,null=True)
    pubg_id = models.CharField(max_length=20,blank=True, null=True)
    points = models.IntegerField(default=0, blank=True,null=True)

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])

    def __str__(self):
        return self.user.username

class Point(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    player = models.ForeignKey(Profile,on_delete=models.CASCADE)
    points = models.IntegerField(default=0, blank=True, null=True)
    reason = models.CharField(max_length=50,blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        player1 = Profile.objects.get(user=self.player.user)
        if self.player == player1:
            player1.points = player1.points + self.points
            player1.save()
        super(Point, self).save(*args, **kwargs)


class MinusPoint(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    player = models.ForeignKey(Profile,on_delete=models.CASCADE)
    points = models.IntegerField(default=0, blank=True, null=True)
    reason = models.CharField(max_length=50,blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        player1 = Profile.objects.get(user=self.player.user)
        if self.player == player1:
            if player1.points  > 0:
                player1.points = player1.points - self.points
                player1.save()
        super(MinusPoint, self).save(*args, **kwargs)