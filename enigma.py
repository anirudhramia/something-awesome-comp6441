from rotor import Rotor
from reflector import Reflector

class EnigmaMachine:
  def __init__(self, num_rotors, plugboard):
    self.rotor1 = Rotor(0, 3, 1)
    self.rotor2 = Rotor(0, 2, 1)
    self.rotor3 = Rotor(0, 1, 1)
    self.rotor4 = Rotor(0, 16, 1)
    self.double_step = False
    self.reflector = Reflector(0)

  def start(self):
    loop = True
    print(chr(self.rotor3.get_position()+96)+ " " + chr(self.rotor2.get_position()+96) + " " + chr(self.rotor1.get_position()+96))
    while loop is True:
      letter = input(">>> ")
      letter = ord(letter)-97
      letter = self.rotor1.passthrough(letter, True)
      letter = self.rotor2.passthrough(letter, True)
      letter = self.rotor3.passthrough(letter, True)
      letter = self.rotor4.passthrough(letter, True)
      letter = self.reflector.passthrough(letter)
      letter = self.rotor4.passthrough(letter, False)
      letter = self.rotor3.passthrough(letter, False)
      letter = self.rotor2.passthrough(letter, False)
      letter = self.rotor1.passthrough(letter, False)
      
      print(chr(letter+97))
      self.rotate_rotors()
      print(chr(self.rotor3.get_position()+96) + " " + chr(self.rotor2.get_position()+96) + " " + chr(self.rotor1.get_position()+96))

  def rotate_rotors(self):
    self.rotor1.rotate()
    if (self.rotor1.get_position() == self.rotor1.get_turnover()+1):
      self.rotor2.rotate()
    if (self.rotor2.get_position() == self.rotor2.get_turnover()+1):
      self.rotor3.rotate()


