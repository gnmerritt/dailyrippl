from django.contrib import admin

from . import models

admin.site.register(models.State)
admin.site.register(models.District)

admin.site.register(models.Representative)
admin.site.register(models.Term)
admin.site.register(models.ContactInfo)
