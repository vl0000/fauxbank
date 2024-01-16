from unittest import TestCase

from tests.data import payment

from database.models import Transaction

class TestTransactions(TestCase):

    def test_can_serialise(self):
        """Tests if the class Transaction can serialise from dict"""
        Transaction(**payment)