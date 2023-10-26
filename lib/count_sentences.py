#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=''):
    self.value = value

  def is_sentence(self):
    last_char = self.value[-1]
    if last_char == ".":
      return True
    else:
      return False
    
  def is_question(self):
    last_char = self.value[-1]
    if last_char == "?":
      return True
    else:
      return False
    
  def is_exclamation(self):
    last_char = self.value[-1]
    if last_char == "!":
      return True
    else:
      return False
    
  def count_sentences(self):
    sentences = 0
    punctuation_marks = set([".", "!", "?"])
    consecutive_marks = 0

    for char in self.value:
      if char in punctuation_marks:
        consecutive_marks += 1
      else:
        if consecutive_marks > 0:
          sentences += 1
          consecutive_marks = 0
    if consecutive_marks > 0:
      sentences += 1

    return sentences


  def get_value(self):
    print(self._value)
    return self._value

  def set_value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  

hello = MyString(value="Hello.")
hello.value
hello.is_sentence()