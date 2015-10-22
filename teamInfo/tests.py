from django.test import TestCase
from django.utils import timezone

import datetime

from .models import Teamer

# Create your tests here.

class TeamerMethodTests(TestCase):

    def test_was_birthday_recently_with_future_question(self):
        """
        was_birthday_recently() should return False for questions whose
        Birthday is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_teamer = Teamer(Birthday=time)
        self.assertEqual(future_teamer.was_birthday_recently(), False)
