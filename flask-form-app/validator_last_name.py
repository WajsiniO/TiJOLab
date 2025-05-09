from register_form_fields import RegisterFormFields
from validator import Validator
from re import *

class LastNameValidator(Validator):
    def __init__(self, last_name):
        self.last_name = last_name

    def is_valid(self):
        if self.last_name is None or self.last_name.strip() == "":
            return False

        regex = r"^[1=.*(A-Z)a-z]{1,}$"
        pattern = compile(regex)
        matcher = pattern.match(self.last_name)

        return bool(matcher)

    def field_name(self):
        return RegisterFormFields.LAST_NAME