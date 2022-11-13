"""users_book = AdressBook : 'Class instanse'
"""

def show_phone(name):
    if name.strip() not in users_book:
        return 'This contact does not exist.'
    return users_book.data[name.casefold()]


def show_name(phone):
    if phone.strip() not in users_book.values():
        return 'This phone does not exist.'
    return users_book.data[phone.casefold()]


def show_all():
    return users_book


def search(data):
    for users in users_book.values():
        for elem in users.phones.value:
            if data in elem:
                return users
        if data in users.name.value:
            return users