from register_form_fields import RegisterFormFields
from validator import Validator
from re import *

class PESELValidator(Validator):
    def __init__(self, PESEL):
        self.PESEL = PESEL
        self.waga = [1,3,7,9,1,3,7,9,1,3]

    def is_valid(self):
        if self.PESEL is None or self.PESEL.strip() == "":
            return False

        regex = r"^[0-9]{11}$"
        pattern = compile(regex)
        matcher = pattern.match(self.PESEL)

        if bool(matcher):
            cyfry = [int(cyfra) for cyfra in self.PESEL[:10]]
            suma = sum(cyfra * waga for cyfra, waga in zip(cyfry, self.waga))
            kontrolna = (10- (suma %10)) % 10
            return str(kontrolna) == self.PESEL[10]
        else:
            return False

    def field_name(self):
        return RegisterFormFields.PESEL