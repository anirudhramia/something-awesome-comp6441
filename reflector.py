class Reflector:
  def __init__(self, num):
    self.position = 1
    if(num == 0): # Reflector B Thin (Bruno)
      self.connections = [[0,4], [1,13], [2,10], [3,16], [4,0], [5,20], [6,24], [7,22], [8,9], [9,8], [10,2], [11,14], [12,15],
       [13,1], [14,11], [15,12], [16,3], [17,23], [18,25], [19,21], [20,5], [21,19], [22,7], [23,17], [24,6], [25,18]]
    elif(num == 1): # Reflector C Thin (Caesar)
      self.connections = [[0,17], [1,3], [2,14], [3,1], [4,9], [5,13], [6,19], [7,10], [8,21], [9,4], [10,7], [11,12], [12,11], 
      [13,5], [14,2], [15,22], [16,25], [17,0], [18,23], [19,6], [20,24], [21,8], [22,15], [23,18], [24,20], [25,16]]

  def passthrough(self, letter):
    converted_letter = self.connections[letter][1]
    return_value = converted_letter
    return return_value

  def rotate(self):
    temp = self.connections.pop(0)
    self.connections.append(temp)
    self.position = self.position + 1
    if(self.position == 27):
      self.position = 1

  def set_position(self, new_position):
    if(new_position > 0 and new_position < 27):
      while(self.position != new_position):
        self.rotate()

  def set_alphabet_ring(self, new_ring_position):
    if(new_ring_position >= 0 and new_ring_position < 26):
      for wire in self.connections:
        wire[0] = wire[0]+1
        if(wire[0] > 25):
          wire[0]=wire[0]-26
        wire[1] = wire[1]+new_ring_position
        if(wire[1] > 25):
          wire[1] = wire[1]-26
    first = self.connections[0][0]
    while first != self.position-1:
      temp = self.connections.pop(0)
      self.connections.append(temp)
      first = self.connections[0][0]