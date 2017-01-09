"""rippl URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .registration.forms import RecaptchaRegView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/register/$', RecaptchaRegView.as_view()),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'go', TemplateView.as_view(template_name='app.html'), name='go'),
    url(
        r'^$',
        TemplateView.as_view(template_name='mission_statement.html'),
        name='mission',
    ),
    url(
        r'^privacy_terms',
        TemplateView.as_view(template_name='tos.html'),
        name='tos',
    ),

    url(r'^legislature/', include('legislature.urls', namespace='leg')),
    url(r'^rippl/', include('questing.urls', namespace='rippl')),
    url(r'^laws/', include('bills.urls', namespace='laws')),
]
