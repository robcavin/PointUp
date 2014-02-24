from django.contrib import admin
from django_facebook.models import FacebookCustomUser

admin.site.register(FacebookCustomUser,admin.ModelAdmin)