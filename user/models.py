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
