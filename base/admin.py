from django.contrib import admin
from .models import Tournament, Round ,Match

# Register your models here.
#admin.site.register(apply)
admin.site.register(Match)
admin.site.register(Round)
admin.site.register(Tournament)