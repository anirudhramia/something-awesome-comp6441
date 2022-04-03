class Plugboard:
  def __init__(self,connections):
      self.connections = connections

  def passthrough(self, letter):
    converted_letter = letter

    for connection in self.connections:
      if (connection[0] == letter):
        converted_letter = connection[1]

    return_value = converted_letter
    return return_value
  
  def add_connection(self, from_letter, to_letter):
    self.connections[from_letter] = (from_letter, to_letter)
    self.connections[to_letter] = (to_letter, from_letter)

  def reset(self,connections):
    self.connections = connections