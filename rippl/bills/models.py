"""Models related to bills """
from django.db import models

from questing.models import Topic
from legislature.models import Representative


class Bill(models.Model):
    sunlight_id = models.CharField(max_length=63)

    official_title = models.TextField()
    popular_title = models.CharField(max_length=127)
    summary = models.TextField()
    url = models.CharField(max_length=127, help_text='Permalink with more info')

    topics = models.ManyToManyField(Topic)

    CHAMBERS = (
        ('S', 'Senate'),
        ('H', 'House'),
    )
    chamber = models.CharField(max_length=3, choices=CHAMBERS)
    sponsor = models.ForeignKey(Representative, on_delete=models.SET_NULL, null=True)