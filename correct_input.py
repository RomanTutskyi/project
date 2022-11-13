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
        

class Email(Field):
    @Field.value.setter
    def value(self, value):
        if re.match(r"[a-zA-Z_+-]+\S{1,}\@[a-zA-Z_+-]+\.[a-zA-Z_+-]{2,}", value).group():
            self._value = value
        else:
            raise ValueError(f' {value} Invalid e-mail')