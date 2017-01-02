"""Models related to bills """
from django.db import models

from questing.models import Topic
from legislature.models import Representative


class Bill(models.Model):
    sunlight_id = models.CharField(max_length=63, default='')

    official_title = models.TextField(default='')
    popular_title = models.CharField(max_length=127, default='')
    summary = models.TextField(default='')
    url = models.CharField(max_length=127, default='', help_text='Permalink with more info')

    CHAMBERS = (
        ('S', 'Senate'),  # TODO(carolyn): match to Representative field
        ('H', 'House'),
    )

    chamber = models.CharField(max_length=3, choices=CHAMBERS, null=True)
    sponsor = models.ForeignKey(Representative, on_delete=models.SET_NULL, null=True)

    topics = models.ManyToManyField(Topic)
