from rotor import Rotor
from config import Config
from reflector import Reflector
from plugboard import Plugboard
class EnigmaMachine:
  def __init__(self, config):
    self.rotor1 = Rotor(config.rotor1_number, config.rotor1_position, config.rotor1_ring_setting) # Fast position: Rotates every keystroke
    self.rotor2 = Rotor(config.rotor2_number, config.rotor2_position, config.rotor2_ring_setting) # Middle
    self.rotor3 = Rotor(config.rotor3_number, config.rotor3_position, config.rotor3_ring_setting) # Slow Position
    self.rotor4 = Rotor(config.rotor4_number, config.rotor4_position, config.rotor4_ring_setting)

    self.rotated = [False, False, False]

    self.reflector = Reflector(config.reflector)
    self.plugboard = Plugboard(config.plugboard)
    self.original_config = config

  def enter_key(self, letter):
    letter = ord(letter)-97

    self.rotate_rotors()

    letter = self.plugboard.passthrough(letter)
    letter = self.rotor1.passthrough(letter, True)
    letter = self.rotor2.passthrough(letter, True)
    letter = self.rotor3.passthrough(letter, True)
    letter = self.rotor4.passthrough(letter, True)
    letter = self.reflector.passthrough(letter)
    letter = self.rotor4.passthrough(letter, False)
    letter = self.rotor3.passthrough(letter, False)
    letter = self.rotor2.passthrough(letter, False)
    letter = self.rotor1.passthrough(letter, False)
    letter = self.plugboard.passthrough(letter)

    return letter

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

  def get_visible_letters(self):
    letters = []
    letters.append(self.rotor4.get_current_letter()+97)
    letters.append(self.rotor3.get_current_letter()+97)
    letters.append(self.rotor2.get_current_letter()+97)
    letters.append(self.rotor1.get_current_letter()+97)
    return letters
  
  def get_rotor_types(self):
    types = []
    types.append(self.rotor4.get_type())
    types.append(self.rotor3.get_type())
    types.append(self.rotor2.get_type())
    types.append(self.rotor1.get_type())
    return types

  def get_reflector(self):
    return self.reflector.get_type()

  def reset(self):
    self.rotor1.configure_rotor(self.original_config.rotor1_number, self.original_config.rotor1_position, self.original_config.rotor1_ring_setting)
    
    self.rotor2.configure_rotor(self.original_config.rotor2_number, self.original_config.rotor2_position, self.original_config.rotor2_ring_setting)

    self.rotor3.configure_rotor(self.original_config.rotor3_number, self.original_config.rotor3_position, self.original_config.rotor3_ring_setting)

    self.rotor4.configure_rotor(self.original_config.rotor4_number, self.original_config.rotor4_position, self.original_config.rotor4_ring_setting)

    self.reflector.reset(self.original_config.reflector)

    self.plugboard.reset(self.original_config.plugboard)


  def new_config(self, config):
    self.original_config = config


