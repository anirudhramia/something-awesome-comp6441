class Reflector:
  def __init__(self, num):
    if(num == 0): # Reflector B Thin (Bruno)
      self.connections = [(0,4), (1,13), (2,10), (3,16), (4,0), (5,20), (6,24), (7,22), (8,9), (9,8), (10,2), (11,14), (12,15), 
      (13,1), (14,11), (15,12), (16,3), (17,23), (18,25), (19,21), (20,5), (21,19), (22,7), (23,17), (24,6), (25,18)]
    elif(num == 1): # Reflector C Thin (Caesar)
      self.connections = [(0,17), (1,3), (2,14), (3,1), (4,9), (5,13), (6,19), (7,10), (8,21), (9,4), (10,7), (11,12), (12,11),
       (13,5), (14,2), (15,22), (16,25), (17,0), (18,23), (19,6), (20,24), (21,8), (22,15), (23,18), (24,20), (25,16)]

  def passthrough(self, letter):
    converted_letter = self.connections[letter][1]
    return_value = converted_letter
    return return_value