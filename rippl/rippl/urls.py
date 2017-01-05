"""rippl URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .registration.forms import RecaptchaRegView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/register/$', RecaptchaRegView.as_view()),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(
        r'^mission_statement',
        TemplateView.as_view(template_name='mission_statement.html'),
    ),
    url(
        r'^profile',
        TemplateView.as_view(template_name='profile.html'),
        name='profile'
    ),

    url(r'^legislature/', include('legislature.urls', namespace='leg')),
    url(r'^rippl/', include('questing.urls', namespace='rippl')),
]
