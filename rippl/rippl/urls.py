"""rippl URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),

    url(r'^legislature/', include('legislature.urls')),
]
