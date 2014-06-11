from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from models import CustomUser
from django.contrib.auth.models import Group

from django.contrib import admin
from rest_framework import viewsets, routers
from points import views

admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'points.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'points.views.home'),
    url(r'^search/', 'points.views.search_results'),
    url(r'^transaction/', 'points.views.transaction'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')),
)