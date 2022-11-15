#Додати до Record()
def change_note(self, text):
    self.note = Note(text)
    
def delete_note(self):
    self.note = Note("")


def change_note(data):
    name, text = data.split(maxsplit=1)
    new_text = input(f"Your previous text: {text}\nEnter new text: ")
    users_book.data[name.casefold()].change_note(new_text)
    return 'Text changed'


