class MyString:
    '''MyString in count_sentences.py'''

    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def count_sentences(self):
        '''returns the number of sentences in the value.'''
        import re
        sentences = re.split(r'[.!?]', self.value)
        return sum(1 for sentence in sentences if sentence.strip())
    
    def is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        return self.value.endswith('.')
    
    def is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        return self.value.endswith('?')
    
    def is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        return self.value.endswith('!')

# Testing the MyString class
'''string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())       # Output: False
print(string.is_question())       # Output: True
print(string.is_exclamation())    # Output: False
print(string.count_sentences())   # Output: 3'''
