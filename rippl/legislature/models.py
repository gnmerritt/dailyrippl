from datetime import date
from django.db import models


class State(models.Model):
    name = models.CharField(db_index=True, max_length=80)
    abbr = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        desc = "at large" if self.number == 0 else self.number
        return "{} {}".format(self.state.abbr, desc)


class Representative(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    # personal info
    gender = models.CharField(max_length=1)
    birthday = models.DateField()
    religion = models.CharField(max_length=80)
    # identifiers in other systems
    google_id = models.CharField(max_length=20)
    bioguide_id = models.CharField(max_length=20, db_index=True)
    wikipedia_id = models.CharField(max_length=60)

    def __str__(self):
        return "{} {} ({})".format(self.first, self.last, self.bioguide_id)


class Term(models.Model):
    HOUSE = 'HOR'
    SENATE = 'SEN'
    BODIES = (
        (SENATE, 'Senate'),
        (HOUSE, 'House of Representatives')
    )
    PARTIES = (
        ('D', 'Democrat'),
        ('R', 'Republican'),
        ('I', 'Independent'),
        ('G', 'Green'),
        ('L', 'Libertarian'),
    )
    rep = models.ForeignKey(Representative, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    chamber = models.CharField(max_length=3, choices=BODIES)
    party = models.CharField(max_length=1, choices=PARTIES)

    def __str__(self):
        return "{}-{}, {}-{}" \
            .format(self.chamber, self.district, self.start, self.end)

    def is_active(self):
        return self.end > date.today()


class ContactInfo(models.Model):
    NETWORKS = (
        ('FB', 'Facebook'),
        ('TWT', 'Twitter'),
        ('WEB', 'Website'),
        ('TEL', 'Telephone number'),
        ('EM', 'Email'),
    )
    rep = models.ForeignKey(Representative, on_delete=models.CASCADE)
    how = models.CharField(max_length=3, choices=NETWORKS)
    addr = models.CharField(max_length=100)
    display = models.CharField(max_length=100, null=True, blank=True)

    def display(self):
        return self.display if self.display else self.addr

    def __str__(self):
        return "{}@{}".format(self.display(), self.how)
