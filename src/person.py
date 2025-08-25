from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, email, phone):
        self._name = name
        self._age = age
        self._email = email
        self._phone = phone

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, value):
        self._phone = value

    @abstractmethod
    def __str__(self):
        pass
    def __repr__(self):
        pass