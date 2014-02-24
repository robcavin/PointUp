from django.contrib import admin
from points.models import CustomUser

admin.site.register(CustomUser,admin.ModelAdmin)