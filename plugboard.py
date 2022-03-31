class Plugboard:
  def __init__(self):
      self.connections = [[0,0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8], [9,9], [10,10], [11,11], [12,12], 
      [13,13], [14,14], [15,15], [16,16], [17,17], [18,18], [19,19], [20,20], [21,21], [22,22], [23,23], [24,24], [25,25]]

  def passthrough(self, letter):
    converted_letter = self.connections[letter][1]
    return_value = converted_letter
    return return_value
  
  def add_connection(self, from_letter, to_letter):
    self.connections[from_letter] = (from_letter, to_letter)
    self.connections[to_letter] = (to_letter, from_letter)

  def reset(self):
    self.connections = [[0,0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8], [9,9], [10,10], [11,11], [12,12],
     [13,13], [14,14], [15,15], [16,16], [17,17], [18,18], [19,19], [20,20], [21,21], [22,22], [23,23], [24,24], [25,25]]