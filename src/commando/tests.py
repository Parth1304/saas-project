from django.conf import settings
from django.test import TestCase


class RDSDBTestCase(TestCase):
    def test_db_url(self):
        DATABASE_URL = settings.DATABASE_URL
        self.assertIn("rds.amazonaws.com", DATABASE_URL)
