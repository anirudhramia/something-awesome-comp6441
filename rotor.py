from collections import deque

class Rotor:
  def __init__(self, rotor_position, rotor_number, position):
    self.rotor_position_in_machine = rotor_position
    self.position = position
    self.notch_position = [26,26]
    self.notch_number = 0 # Used for rotors VI, VII and VIII which have two notches
    self.notch_engaged = False
    self.connections = {}
    self.rotor_type = ""
    self.configure_rotor(rotor_number) # Configure the input/output connections and turnover point for the rotor based on rotor number


  def passthrough(self, letter, forward):
    if (forward):
      compare_letter = self.connections[letter][1]
      index = 0
      for wire in self.connections:
        if(wire[0] == compare_letter):
          converted_letter = index
          break
        index = index + 1
      return_value = converted_letter
    else:
      compare_letter = self.connections[letter][0]
      index = 0
      for wire in self.connections:
        if(wire[1] == compare_letter):
          converted_letter = index
          break
        index = index + 1

      return_value = converted_letter

    return return_value

  def rotate(self):
    temp = self.connections.pop(0)
    self.connections.append(temp)
    self.position = self.position + 1
    if(self.position == 27):
      self.position = 1

  def get_position(self):
    return self.position

  def set_position(self, new_position):
    if(new_position > 0 and new_position < 27):
      while(self.position != new_position):
        self.rotate()

  def set_alphabet_ring(self, new_ring_position):
    if(new_ring_position >= 0 and new_ring_position < 26):
      for wire in self.connections:
        wire[0] = wire[0]+new_ring_position
        if(wire[0] > 25):
          wire[0] = wire[0]-26

  def get_current_letter(self):
    return self.connections[0][0]

  def get_notch_position(self):
    return self.notch_position[self.notch_number]
  
  def change_notch(self):
    # This logic switches between the two returned notch values
    # For rotors I-V and Beta and Gamma, it has no effect
    # For rotors VI-VIII, it switches between the two notch positions
    if (self.notch_number == 0):
      self.notch_number = 1
    elif (self.notch_number == 1):
      self.notch_number = 0
    else:
      self.notch_number = 1

  def set_notch_engaged(self, engage):
    self.notch_engaged = engage

  def get_notch_engaged(self):
    return self.notch_engaged

  def configure_rotor(self, rotor_number):
    if (rotor_number == 1):
      self.rotor_type = "I"
      self.connections = [[0,4], [1,10], [2,12], [3,5], [4,11], [5,6], [6,3], [7,16], [8,21], [9,25], [10,13], [11,19], [12,14],
       [13,22], [14,24], [15,7], [16,23], [17,20], [18,18], [19,15], [20,0], [21,8], [22,1], [23,17], [24,2], [25,9]]
      self.notch_position = [17,17]

    elif (rotor_number == 2):
      self.rotor_type = "II"
      self.connections = [[0,0], [1,9], [2,3], [3,10], [4,18], [5,8], [6,17], [7,20], [8,23], [9,1], [10,11], [11,7], [12,22], 
      [13,19], [14,12], [15,2], [16,16], [17,6], [18,25], [19,13], [20,15], [21,24], [22,5], [23,21], [24,14], [25,4]]
      self.notch_position = [5,5]

    elif (rotor_number == 3):
      self.rotor_type = "III"
      self.connections = [[0,1], [1,3], [2,5], [3,7], [4,9], [5,11], [6,2], [7,15], [8,17], [9,19], [10,23], [11,21], [12,25],
       [13,13], [14,24], [15,4], [16,8], [17,22], [18,6], [19,0], [20,10], [21,12], [22,20], [23,18], [24,16], [25,14]]
      self.notch_position = [22,22]

    elif (rotor_number == 4):
      self.rotor_type = "IV"
      self.connections = [[0,4], [1,18], [2,14], [3,21], [4,15], [5,25], [6,9], [7,0], [8,24], [9,16], [10,20], [11,8], [12,17], 
      [13,7], [14,23], [15,11], [16,13], [17,5], [18,19], [19,6], [20,10], [21,3], [22,2], [23,12], [24,22], [25,1]]
      self.notch_position = [10,10]

    elif (rotor_number == 5):
      self.rotor_type = "V"
      self.connections = [[0,21], [1,25], [2,1], [3,17], [4,6], [5,8], [6,19], [7,24], [8,20], [9,15], [10,18], [11,3], [12,13],
       [13,7], [14,11], [15,23], [16,0], [17,22], [18,12], [19,9], [20,16], [21,14], [22,5], [23,4], [24,2], [25,10]]
      self.notch_position = [26,26]

    elif (rotor_number == 6):
      self.rotor_type = "VI"
      self.connections = [[0,9], [1,15], [2,6], [3,21], [4,14], [5,20], [6,12], [7,5], [8,24], [9,16], [10,1], [11,4], [12,13],
       [13,7], [14,25], [15,17], [16,3], [17,10], [18,0], [19,18], [20,23], [21,11], [22,8], [23,2], [24,19], [25,22]]
      self.notch_position = [13,26]

    elif (rotor_number == 7):
      self.rotor_type = "VII"
      self.connections = [[0,13], [1,25], [2,9], [3,7], [4,6], [5,17], [6,2], [7,23], [8,12], [9,24], [10,18], [11,22], [12,1], 
      [13,14], [14,20], [15,5], [16,0], [17,8], [18,21], [19,11], [20,15], [21,4], [22,10], [23,16], [24,3], [25,19]]
      self.notch_position = [13,26]

    elif (rotor_number == 8):
      self.rotor_type = "VIII"
      self.connections = [[0,5], [1,10], [2,16], [3,7], [4,19], [5,11], [6,23], [7,14], [8,2], [9,1], [10,9], [11,18], [12,15], 
      [13,3], [14,25], [15,17], [16,0], [17,12], [18,4], [19,22], [20,13], [21,8], [22,20], [23,24], [24,6], [25,21]]
      self.notch_position = [13,26]

    elif(rotor_number == 16): # Beta Rotor (Used specifically in M4 Engima and did not rotate)
      self.rotor_type = "Beta"
      self.connections = [[0,11], [1,4], [2,24], [3,9], [4,21], [5,2], [6,13], [7,8], [8,23], [9,22], [10,15], [11,1], [12,16], 
      [13,12], [14,3], [15,17], [16,19], [17,0], [18,10], [19,25], [20,6], [21,5], [22,20], [23,7], [24,14], [25,18]]

    elif(rotor_number == 17): # Gamma Rotor (Used specifically in M4 Engima and did not rotate)
      self.rotor_type = "Gamma"
      self.connections = [[0,5], [1,18], [2,14], [3,10], [4,0], [5,13], [6,20], [7,4], [8,17], [9,7], [10,12], [11,1], [12,19], 
      [13,8], [14,24], [15,2], [16,22], [17,11], [18,16], [19,15], [20,25], [21,23], [22,21], [23,6], [24,9], [25,3]]
      self.notch_position = [26,26]

    else:
      self.rotor_type = "Default"
      self.connections =  [[0,0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8], [9,9], [10,10], [11,11], [12,12], 
      [13,13], [14,14], [15,15], [16,16], [17,17], [18,18], [19,19], [20,20], [21,21], [22,22], [23,23], [24,24], [25,25]]
      self.notch_position = [26,26]
      