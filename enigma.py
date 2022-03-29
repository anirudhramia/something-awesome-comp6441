from rotor import Rotor
from reflector import Reflector

class EnigmaMachine:
  def __init__(self, num_rotors, plugboard):
    self.rotor1 = Rotor(0, 5, 1)
    self.rotor2 = Rotor(0, 2, 1)
    self.rotor3 = Rotor(0, 3, 1)
    self.rotor4 = Rotor(0, 4, 1)
    # self.rotors = []
    # self.setup_rotors(num_rotors)
    self.reflector = Reflector(0)

  def start(self):
    loop = True
    print(chr(self.rotor1.get_current_letter()+97)+ " " + chr(self.rotor2.get_current_letter()+97) + " " + chr(self.rotor3.get_current_letter()+97))
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
      print(chr(self.rotor1.get_current_letter()+97) + " " + chr(self.rotor2.get_current_letter()+97) + " " + chr(self.rotor3.get_current_letter()+97))

  # def setup_rotors(self, num_rotors):
  #   ids=[]

  def rotate_rotors(self):
    self.rotor1.rotate()
    if (self.rotor1.get_position() == self.rotor1.get_turnover()):
      self.rotor2.rotate()
      if (self.rotor2.get_position() == self.rotor2.get_turnover()):
        self.rotor3.rotate()
        if (self.rotor3.get_position() == self.rotor3.get_turnover()):
          self.rotor4.rotate()
