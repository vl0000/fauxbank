from unittest import TestCase
from sqlalchemy import insert, select

from tests.data import payment, query
from database.tables import transactions
from database.models import Transaction

class TestTransactions(TestCase):

    def setUp(self):
        insert(transactions).values({"id": 123, "payer": 100, "payee": 101, "amount": 10.0})

    def test_can_serialise(self):
        """Tests if the class Transaction can serialise from dict"""
        Transaction(**payment)

    def test_can_insert(self):
        """Checks if it is possible to insert a payment into the db"""
        transaction = Transaction(**payment).model_dump()
        stmt = insert(transactions).values(transaction)
        query(stmt)

    def test_in_db(self):
        res = select(transactions).where(transactions.c.id == 123)
        self.assertIsNotNone(res)