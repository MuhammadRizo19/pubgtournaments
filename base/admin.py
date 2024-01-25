from django.contrib import admin
from .models import Tournament, Round ,Match, Participant, Request

# Register your models here.
#admin.site.register(apply)
admin.site.register(Match)
admin.site.register(Request)
admin.site.register(Round)
admin.site.register(Participant)
admin.site.register(Tournament)