# Поєднати з Fields()
class Note(Field):   
    def __repr__(self):
        return f"{self._value}"
    
    @Field.value.setter
    def value(self, value):
        self._value = value

# Додати до классу Record(note : 'Note' = "")
self.note = note

def add_note(self, text):
    self.note = Note(text)
    

#Десь у основній частині
def add_note(data):
    name, text = data.split(maxsplit=1)
    users_book.data[name.casefold()].add_note(text)
    return 'Added successfully'