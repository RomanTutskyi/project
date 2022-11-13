#Треба додати ще пару методів до классу Record()
def add_email(self, data):
    self.email = Email(data)
        
def delete_email(self, data):
    self.email = ""
    
    
#Робота з редагування і видалення

def add_contact(data):
    """Заповнюємо записну книжку (Ім'я, *номер телефону, *день народженя)"""
    name, phone =data_splitter(data)
    new_record = Record(name, phone)
    
    users_book.add_record(new_record)
    return 'New contact added'

def change_contact(data):
    """Змінюємо контактні данні"""
    name, *phone = data.split()

    users_book.data[name.casefold()].change(phone)
    return 'Contact changed'


def add_new_phone(data):
    """Додаємо телефонний номер до вже створенного контакту"""
    name, phone = data_splitter(data)
    users_book.data[name.casefold()].add_phone(phone)
    return f'A new phone: {phone}, has been added to contact name: {name}.'


def delete_func(data):
    """Видаляємо контак із записної книжки із телефоном(нами)"""
    name, phone = data_splitter(data)
    record_delete = users_book.data[name.casefold()]

    if record_delete.remove(phone) is True:
        return f'Contact name: {name} phone: {phone}, has been deleted.'
    else:
        return 'The phone number not exist'
    
def add_birthday(data):
    name, date_of_birthday = data.split()
    print(date_of_birthday)
    users_book.data[name.casefold()].add_birthday(date_of_birthday)
    return 'Birthday added'
    
    
def add_email(data):
    """Додаємо електронну адресу"""
    name, email = data.split()
    users_book.data[name.casefold()].add_email(email)
    return f'A new email: {email}, has been added to contact name: {name}.'


def change_email(data):
    """Змінюємо електронну адресу"""
    name, email = data.split()
    users_book.data[name.casefold()].add_email(email)
    return 'Email changed'


def delete_email(data):
    """Видаляємо електронну адресу"""
    name, email = data.split()
    users_book.data[name.casefold()].delete_email(email)
    return 'Email deleted'


# BONUS func
def data_splitter(data):
    name, phone = data.split() if len(data.split()) > 1 else [data, None]
    return name, phone