from datetime import datetime, timedelta

from django.test import TestCase
from django.core.exceptions import ValidationError

from . import models


class StateTest(TestCase):
    def test_model_str_is_name(self):
        ma = models.State(name='Massachusetts', abbr='MA')
        self.assertEquals(ma.abbr, 'MA')
        self.assertEquals(repr(ma), '<State: Massachusetts>')

    def test_abbr_length(self):
        with self.assertRaises(ValidationError):
            models.State(abbr='too long').full_clean()


class TermTest(TestCase):
    def test_is_active(self):
        past = datetime.now() - timedelta(days=5)
        term = models.Term(end=past.date())
        self.assertFalse(term.is_active())

        future = datetime.now() + timedelta(days=1)
        active_term = models.Term(end=future.date())
        self.assertTrue(active_term.is_active())
