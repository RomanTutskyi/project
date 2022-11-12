from os import system
from collections import UserDict
from datetime import date
import pickle


class Field:
    def __init__(self):
        self._value = ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class Birthday(Field):
    def __init__(self, arg):
        if arg:
            day, month, year = arg.split('.')
            self.value = date(day=int(day), month=int(month), year=int(year))
        else:
            self.value = None


class AdressBook(UserDict):
    N = 0
    cur = 0
    all_values = []

    def __init__(self):
        super().__init__()
        self.book = []

    @property
    def save_data(self):
        with open('data.bin', 'wb') as file_in:
            pickle.dump(self.data, file_in)

    @property
    def unpacking_data(self):
        with open('data.bin', 'rb') as file_out:
            self.data = pickle.load(file_out)

    def in_data(self, name):
        return name in self.data

    def add_record(self, record):
        self.data[record.name.value] = record

    def iteration(self, count):
        self.N += count

        for name, value in self.data.items():
            for value in self.data[name].phones:
                self.book.append(value.value)

    def __next__(self):
        if self.cur < self.N:
            self.cur += 1
            return self.book[self.cur]
        else:
            raise StopIteration


class Record(Field):
    def __init__(self, in_name, in_phone=None, birthsday=None):
        self.cur = 0
        self.N = 3
        self.name = Name(in_name)
        self.phones = []
        self.brt = Birthday(birthsday)
        if in_phone != None:
            self.phones.append(Phone(in_phone))

    def add_birthday(self, date):
        self.brt = Birthday(date)

    def days_to_birthday(self):
        self.cur_date = date.today()
        if self.cur_date.month < self.brt.value.month:
            self.delta_days = date(
                day=int(self.brth.day), month=int(self.brth.month), year=int(self.cur_date.year))
            return (self.delta_days - self.cur_date).days

        else:
            self.delta_days = date(
                day=int(self.brt.value.day), month=int(self.brt.value.month), year=int(self.cur_date.year)+1)
            return (self.delta_days - self.cur_date).days

    def add_phone(self, phone=None):
        self.phones.append(Phone(phone))

    def change(self, old_note, new_note):
        for old in self.phones:
            if old.value == old_note:
                self.phones.remove(old)
                self.phones.append(Phone(new_note))

    def remove_phone(self, phone):
        for old in self.phones:
            if old.value == phone:
                self.phones.remove(old)