from enigma import EnigmaMachine
from tkinter import *

# Rotor Options:
# Rotors I, II, III, IV, V, VI, VII and VIII are represented by their respective numerical value. (1,2,3,4,5,6,7,8)
# The Beta Rotor and the Gamma Rotor, which were made specifically for use as the fourth rotor in 
# the M4 Enigma machine are represented by 16 and 17 respectively. These rotors do not turn.

# Reflector Options:
# The M4 had two reflector options: Reflector B Thin and Reflector C Thin. They were also known
# as Bruno and Caesar respectively. Bruno is 0 and Caesar is 1.

# Online Simulator to test correct output
# http://people.physik.hu-berlin.de/~palloks/js/enigma/enigma-u_v26_en.html 
# OR
# https://cryptii.com/pipes/enigma-machine
# (Remember to select M4 "Shark")

# Rotor Options
# I: 1
# II: 2
# III: 3
# IV: 4
# V: 5
# VI: 6
# VII: 7
# VIII: 8

# Fourth Rotor Options
# Beta: 16
# Gamma: 17

# Reflectors
# Bruno: 0 (B Thin)
# Caesar: 1 (C Thin)

# Input is Reflector, followed by array of Rotors in reverse order

class Screen:
  def __init__(self,width,height,title):
    self.root = Tk()
    self.root.title(title)
    self.width = width
    self.height = height
    self.enigma = EnigmaMachine(0, [16, 3, 2, 1],True)
#                      Ref, 4, 3, 2, 1

    # Set width and height
    self.root.geometry('%dx%d' % (width, height))
    self.root.minsize(width,height)
    self.root.maxsize(width,height)

    # Setup canvas
    self.canvas = Canvas(self.root, bg="#3e3e3e", width=self.width, height=self.height, highlightthickness=0)

  # Draw keyboard
  def draw_key(self,x,y,r,key):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return self.canvas.create_oval(x0,y0,x1,y1,fill='#292929', outline='black',width=5)

  def draw_keyboard(self):
    keyboard=['qwertzuio','asdfghjk','pyxcvbnml']
    initial_x=[85,160,85]
    initial_y=[375,500,635]
    gap = 140
    row_num = 0
    for row in keyboard:
      x = initial_x[row_num]
      y = initial_y[row_num]
      for key in row:
        self.draw_key(x,y,50,key)
        self.canvas.create_text(x,y,fill="white", font="sans 30 bold", text=key.capitalize())
        x = x+gap
      row_num = row_num+1

  def test():
    print("test")

  def run(self):
    self.draw_keyboard()
    self.root.bind('<KeyPress>', self.test)
    self.canvas.pack(side="bottom")
    self.root.mainloop()

# Main Loop
screen = Screen(1280,720,'Enigma Machine - M4 Shark')
screen.run()