from msilib import knownbits
from platform import machine
from rotor import Rotor
from reflector import Reflector

# Rotor Options:
# Rotors I, II, III, IV, V, VI, VII and VIII are represented by their respective numerical value.
# The Beta Rotor and the Gamma Rotor, which were made specifically for use as the fourth rotor in 
# the M4 Enigma machine are represented by 16 and 17 respectively. These rotors do not turn.

# Reflector Options:
# The M4 had two reflector options: Reflector B Thin and Reflector C Thin. They were also known
# as Bruno and Caesar respectively. Bruno is 0 and Caesar is 1.


class EnigmaMachine:
  def __init__(self, plugboard):
    self.rotor1 = Rotor(1, 3, 1)
    self.rotor2 = Rotor(2, 2, 1)
    self.rotor3 = Rotor(3, 1, 1)
    self.rotor4 = Rotor(4, 16, 1)
    self.rotated = [False, False, False]
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
    self.rotor1.rotate() #Fast rotor: Meaning it turns every keystroke
    self.rotated[0] = True

    if(self.rotor2.get_notch_engaged() == True):
      self.rotor2.rotate()
      self.rotor2.set_notch_engaged(False)
      self.rotated[1] = True
      if(self.rotated[0] == False):
        self.rotor1.rotate()
        self.rotated[0] = True
    
    if(self.rotor3.get_notch_engaged() == True):
      self.rotor3.rotate()
      self.rotor3.set_notch_engaged(False)
      self.rotated[2] = True
      if(self.rotated[1] == False):
        self.rotor2.rotate()
        self.rotated[1] = True

    if (self.rotor1.get_position() == self.rotor1.get_notch_position()):
      self.rotor2.set_notch_engaged(True)
    if (self.rotor2.get_position() == self.rotor2.get_notch_position()):
      self.rotor3.set_notch_engaged(True)

    self.rotated = [False, False, False]

    
    # In the M4 Enigma machine, the 4th rotor does not rotate along with the reflector. Hence no logic to rotate it



