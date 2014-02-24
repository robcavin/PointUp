from django.contrib import admin
from django_facebook.models import FacebookCustomUser
from django.contrib.auth.admin import UserAdmin
from points.models import Person

admin.site.register(FacebookCustomUser,admin.ModelAdmin)