from unittest import main, TestLoader, TestSuite
from tests import test_accounts, test_transactions


suite = TestSuite()
loader = TestLoader()

suite.addTests(loader.loadTestsFromModule(test_accounts))
suite.addTests(loader.loadTestsFromModule(test_transactions))

main(defaultTest="suite", verbosity=3)