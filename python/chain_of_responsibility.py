#!/usr/bin/env python


from abc import ABC, abstractmethod


class PasswordValidator(ABC):
    @abstractmethod
    def set_next_validator(self, next_validator):
        pass

    @abstractmethod
    def validate(self, password):
        pass


class LengthValidator(PasswordValidator):
    def set_next_validator(self, next_validator):
        self.next_validator = next_validator

    def validate(self, password):
        if len(password) < 8:
            return False
        if self.next_validator:
            return self.next_validator.validate(password)
        return True


class NumberValidator(PasswordValidator):
    def set_next_validator(self, next_validator):
        self.next_validator = next_validator

    def validate(self, password):
        if not any(char.isdigit() for char in password):
            return False
        if self.next_validator:
            return self.next_validator.validate(password)
        return True


class UppercaseValidator(PasswordValidator):
    def set_next_validator(self, next_validator):
        self.next_validator = next_validator

    def validate(self, password):
        if not any(char.isupper() for char in password):
            return False
        return True


def chain_of_responsibility():
    uppercase_validator = UppercaseValidator()
    number_validator = NumberValidator()
    length_validator = LengthValidator()

    uppercase_validator.set_next_validator(number_validator)
    number_validator.set_next_validator(length_validator)

    password = "Abc12345"
    if uppercase_validator.validate(password):
        print("Password is valid.")
    else:
        print("Password is not valid.")


chain_of_responsibility()
