from django.contrib import admin

from . import models

admin.site.register(models.Topic)

admin.site.register(models.Quest)
admin.site.register(models.QuestAttempt)
admin.site.register(models.QuestStats)
