from unittest import TestCase
from database.models import AccountInDb
from tests.data import fulano

class TestAccounts(TestCase):

    def test_can_serialise(self):
        """Checks wether or not AccountInDB can create a class from a dict"""
        AccountInDb(**fulano)
    
    def test_password_hashes(self):
        """Checks wether the _secure_password function will hash the password"""
        unhashed = fulano["password"]
        acc = AccountInDb(**fulano)
        acc._secure_password()

        self.assertNotEqual(unhashed, acc.password, "The password was not hashed")
