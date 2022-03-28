class Reflector:
  def __init__(self):
    self.connections =  {0:4, 1:9, 2:12, 3:25, 4:0, 5:11, 6:24, 7:23, 8:21, 9:1, 10:22, 11:5,
   12:2, 13:17, 14:16, 15:20, 16:14, 17:13, 18:19, 19:18, 20:15, 21:8, 22:10, 23:7, 24:6, 25:3}

  def passthrough(self, letter):
    converted_letter = self.connections[letter]
    return_value = converted_letter
    return return_value