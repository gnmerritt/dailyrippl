from django.db import models
from django.contrib.auth.models import User

from legislature import models as lm

"""Models for the civic engagement site.

These are free to have foreign key dependencies on data in the legislature app.
"""


class Topic(models.Model):
    """A cause/issue that users may care about"""
    name = models.CharField(db_index=True, max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Quest(models.Model):
    """The UI will likely refer to these as 'ripples'"""
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    rep = models.ForeignKey(lm.Representative, null=True,
                            on_delete=models.CASCADE)

    class Meta(object):
        ordering = ["-created"]

    def __str__(self):
        return "{}: {}...".format(self.name, self.desc[:15])


class QuestAttempt(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    district = models.ForeignKey(lm.District, null=True,
                                 on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True)


class QuestStats(models.Model):
    """Metrics for how many people have attempted a quest"""
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    attempts = models.IntegerField()
    duration = models.DurationField()
