import unittest
from src.ATM import ATM

class ATMTest(unittest.TestCase):

    def setUp(self):
        self.user = ATM(1234,1000)

    def test_raise_error_when_invalid_pin_to_check_balance(self):
        pin = 12345
        self.assertEqual(self.user.check_balance(pin), 1000)

    def test_when_valid_pin_to_check_balance(self):
        pin = 1234
        self.assertEqual(self.user.check_balance(pin), 1000)

    def test_raise_error_when_invalid_pin_to_deposit(self):
        pin = 12345
        amount = 1000
        self.assertEqual(self.user.deposit(pin, amount), None)

    def test_when_valid_pin_to_deposit(self):
        pin = 1234
        amount = 100
        self.assertEqual(self.user.deposit(pin, amount), 1100)

    def test_raise_error_when_invalid_pin_to_withdraw(self):
        pin = 12345
        amount = 1000
        self.assertEqual(self.user.withdraw(pin, amount), None)

    def test_when_valid_pin_to_withdraw(self):
        pin = 1234
        amount = 100
        self.assertEqual(self.user.withdraw(pin, amount), 900)

    def tearDown(self):
        self.user = None