from collections import UserDict
from datetime import date
import pickle
import os
import re

class AddressBook(UserDict):
    N = 0
    cur = 0

    def __init__(self):
        super().__init__()
        self.book = []
        
    def save_data(self):
        with open('adress_book.bin', 'wb') as file_in:
            pickle.dump(self.data, file_in)
    
    def unpack_data(self):
        if os.path.exists('adress_book.bin'):
            with open('adress_book.bin', 'rb') as file_out:
                self.data = pickle.load(file_out)
        else:
            self.data = {}
    
    def find_contact(self, name):
        return self.data[name]
    
    def add_record(self, record:object):
        self.data[record.name.value] = record
        
    def iterator(self, number_of_entries):
        self.N += number_of_entries

        for name, phone in self.data.items():
            for value in self.data[name].phones:
                self.book.append(phone.value)
                
    def __next__(self):
        if self.cur < self.N:
            self.cur += 1
            return self.book[self.cur-1]
        else:
            raise StopIteration


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    

class Name(Field):
    def __repr__(self):
        return f"{self._value}"
    
    @Field.value.setter
    def value(self, value):
        #print('Good')
        self._value = value


class Phone(Field):
    def __repr__(self):
        return f"{''.join(self.value)}"
    
    @Field.value.setter
    def value(self, value):
        #Field.__value = value
        
        if value[0].isnumeric():
            #print('Good2')
            if not value.startswith('+38'):
                value = '+38' + value
            if len(value) != 13:
                pass
                #raise ValueError
            self._value = value
        else:
            print('OOPS')
            raise ValueError


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        if value:
            day, month, year = value.split('.')
            users_birthday = date(day=int(day), month=int(month), year=int(year))
            
            if users_birthday > date.today():
                raise ValueError(f' {users_birthday} Invalid birtday data')
            else:
                self._value = users_birthday
            
    def __repr__(self):
        return f"{self._value.strftime('%A %d %B %Y')}"
    
class Email(Field):
    @Field.value.setter
    def value(self, value):
        if re.match(r"[a-zA-Z_+-]+\S{1,}\@[a-zA-Z_+-]+\.[a-zA-Z_+-]{2,}", value).group():
            self._value = value
        else:
            raise ValueError(f' {value} Invalid e-mail')
        
    def __repr__(self) -> str:
        return f"{self._value}"
    

class Record:
    def __init__(self, name: 'Name', phone: 'Phone' = None, birthday: 'Birthday' = None, email: 'Email' = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday
        self.email = email
        
        if phone:
            self.add_phone(phone)
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        for class_phone in self.phones:
            if class_phone.value == phone.value:
                self.phones.remove(class_phone)
        
    def change(self, phone):
        self.remove_phone(Phone(phone[0]))
        self.add_phone(phone[1])
        
    def add_birthday(self, date):
        self.birthday = Birthday(date)
        
    def days_to_birthday(self):
        self.cur_date = date.today()
        if self.cur_date.month < self.birthday.value.month:
            self.delta_days = date(
                day=int(self.birthday.value.day), month=int(self.birthday.value.month), year=int(self.cur_date.year))
            return (self.delta_days - self.cur_date).days

        else:
            self.delta_days = date(
                day=int(self.birthday.value.day), month=int(self.birthday.value.month), year=int(self.cur_date.year)+1)
            return (self.delta_days - self.cur_date).days
        
    def add_email(self, data):
        self.email = Email(data)
    
    def __repr__(self):
        return (' , '.join(repr(phone) for phone in self.phones) + ' : ' + repr(self.birthday) + ' : ' + repr(self.email) )


