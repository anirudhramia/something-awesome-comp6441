from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard
class EnigmaMachine:
  def __init__(self, reflector_num, rotor_nums,  plugboard):
    self.rotor1 = Rotor(1, rotor_nums[3], 1) # Fast position: Rotates every keystroke
    self.rotor2 = Rotor(2, rotor_nums[2], 1) # Middle
    self.rotor3 = Rotor(3, rotor_nums[1], 1) # Slow Position
    self.rotor4 = Rotor(4, rotor_nums[0], 1)
    self.rotated = [False, False, False]
    self.reflector = Reflector(reflector_num)
    if(plugboard == True):
      self.plugboard = Plugboard()
    else:
      self.plugboard = None
    

  def start(self):
    loop = True
    #print(chr(self.rotor3.get_position()+96)+ " " + chr(self.rotor2.get_position()+96) + " " + chr(self.rotor1.get_position()+96))
    while loop is True:
      letter = input(">>> ")
      letter = ord(letter)-97
      #print(chr(letter+97))
      
      print(chr(self.rotor3.get_position()+96) + " " + chr(self.rotor2.get_position()+96) + " " + chr(self.rotor1.get_position()+96))
      if (self.plugboard != None):
        letter = self.plugboard.passthrough(letter)
      letter = self.rotor1.passthrough(letter, True)
      print(chr(letter+97))
      letter = self.rotor2.passthrough(letter, True)
      print(chr(letter+97))
      letter = self.rotor3.passthrough(letter, True)
      print(chr(letter+97))
      letter = self.rotor4.passthrough(letter, True)
      print(chr(letter+97))
      letter = self.reflector.passthrough(letter)
      print(chr(letter+97))
      letter = self.rotor4.passthrough(letter, False)
      print(chr(letter+97))
      letter = self.rotor3.passthrough(letter, False)
      print(chr(letter+97))
      letter = self.rotor2.passthrough(letter, False)
      print(chr(letter+97))
      letter = self.rotor1.passthrough(letter, False)
      print(chr(letter+97))
      if (self.plugboard != None):
        letter = self.plugboard.passthrough(letter)
      print()
      print(chr(letter+97))
      self.rotate_rotors()
      

  def rotate_rotors(self):
    self.rotor1.rotate()
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
      self.rotor1.change_notch()
      self.rotor2.set_notch_engaged(True)
    if (self.rotor2.get_position() == self.rotor2.get_notch_position()):
      self.rotor2.change_notch()
      self.rotor3.set_notch_engaged(True)

    self.rotated = [False, False, False]

    
    # In the M4 Enigma machine, the 4th rotor does not rotate along with the reflector. Hence no logic to rotate it



