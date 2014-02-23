from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'points.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'points.views.home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^facebook/', include('django_facebook.urls')),
                       url(r'^accounts/', include('django_facebook.auth_urls')),
                       )