
class Config:
  def __init__(self, rotor1, rotor2, rotor3, rotor4, reflector, plugboard):
    self.rotor1_number = rotor1[0]
    self.rotor1_position = rotor1[1]
    self.rotor1_ring_setting = rotor1[2]

    self.rotor2_number = rotor2[0]
    self.rotor2_position = rotor2[1]
    self.rotor2_ring_setting = rotor2[2]

    self.rotor3_number = rotor3[0]
    self.rotor3_position = rotor3[1]
    self.rotor3_ring_setting = rotor3[2]


    self.rotor4_number = rotor4[0]
    self.rotor4_position = rotor4[1]
    self.rotor4_ring_setting = rotor4[2]


    self.reflector = reflector

    self.plugboard = plugboard
  
  def __str__(self):
    string = str(self.rotor1_number) + " " + str(self.rotor1_ring_setting) + " " + str(self.rotor1_position) + "\n" + str(self.rotor2_number) + " " + str(self.rotor2_ring_setting) + " " + str(self.rotor2_position) + "\n" + str(self.rotor3_number) + " " + str(self.rotor3_ring_setting) + " " + str(self.rotor3_position) + "\n" + str(self.rotor4_number) + " " + str(self.rotor4_ring_setting) + " " + str(self.rotor4_position) + "\n" + str(self.reflector) + "\n" + str(self.plugboard) +"\n"
    #string = str(self.rotor1_number)
    return string