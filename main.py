from enigma import EnigmaMachine
from config import Config
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
    self.current_page = 'main'
    
    # self.enigma = EnigmaMachine(0, [16, 3, 2, 1], [])
#                      Ref, 4, 3, 2, 1
    self.enigma = EnigmaMachine(Config(
      [1,1,1],
      [2,1,1],
      [3,1,1],
      [16,1,1],
      0,
      []
    ))

    # Set width and height
    self.root.geometry('%dx%d' % (width, height))
    self.root.minsize(width,height)
    self.root.maxsize(width,height)

    # Setup canvas
    self.canvas = Canvas(self.root, bg="#303030", width=self.width, height=self.height, highlightthickness=0)

    # Lampboard variables
    self.keyboard=[]
    self.key_coords=[]
    self.set_key_coords()

    # Rotor variables
    self.visible_letters=self.enigma.get_visible_letters()
    self.visible_text=[]

    # Setup Buttons
    self.main_buttons = []
    self.config_buttons = []

    ### Main
    # Configure Button
    self.main_buttons.append(Button(self.canvas, text="Configure Machine", command=self.draw_configure_screen))

    # Reset Button
    self.main_buttons.append(Button(self.canvas, text="Reset", command=self.reset))

    ### Config
    # Save and return to enigma screen
    self.config_buttons.append(Button(self.canvas, text='Save', command=self.update_enigma))
    # Return to Enigma screen without saving config
    self.config_buttons.append(Button(self.canvas, text="Cancel", command=self.draw_enigma))

    # Reset to default view
    self.draw_enigma()

# Screen change functions
  # Screen with configure options
  def draw_configure_screen(self):
    self.canvas.delete('all')
    self.switch_to('config')

    self.canvas.create_oval(40, 100, 40, 100,fill='#9c9c9c',outline='#a6a6a6',width=5,tags='rotor')

  # Screen with enigma machine
  def draw_enigma(self):
    self.canvas.delete('all')
    self.switch_to('main')
    r1_x = 140
    r2_x = 290
    r3_x = 440
    r4_x = 590
    y = 150

    # Draw Keyboard
    self.draw_keyboard()

    # Draw Rotors

    # Draw ovals
    self.canvas.create_oval(r1_x-40, y-100, r1_x+40, y+100,fill='#9c9c9c',outline='#a6a6a6',width=5,tags='rotor')
    self.canvas.create_oval(r2_x-40, y-100, r2_x+40, y+100,fill='#9c9c9c',outline='#a6a6a6',width=5,tags='rotor')
    self.canvas.create_oval(r3_x-40, y-100, r3_x+40, y+100,fill='#9c9c9c',outline='#a6a6a6',width=5,tags='rotor')
    self.canvas.create_oval(r4_x-40, y-100, r4_x+40, y+100,fill='#9c9c9c',outline='#a6a6a6',width=5,tags='rotor')

    # Draw bolts
    self.canvas.create_oval(r1_x-10, y-95, r1_x+10, y-75,fill='#633803',width=0,tags='rotor')
    self.canvas.create_oval(r1_x-10, y+75, r1_x+10, y+95,fill='#633803',width=0,tags='rotor')
    self.canvas.create_oval(r2_x-10, y-95, r2_x+10, y-75,fill='#633803',width=0,tags='rotor')
    self.canvas.create_oval(r2_x-10, y+75, r2_x+10, y+95,fill='#633803',width=0,tags='rotor')
    self.canvas.create_oval(r3_x-10, y-95, r3_x+10, y-75,fill='#633803',width=0,tags='rotor')
    self.canvas.create_oval(r3_x-10, y+75, r3_x+10, y+95,fill='#633803',width=0,tags='rotor')
    self.canvas.create_oval(r4_x-10, y-95, r4_x+10, y-75,fill='#633803',width=0,tags='rotor')
    self.canvas.create_oval(r4_x-10, y+75, r4_x+10, y+95,fill='#633803',width=0,tags='rotor')

    # Draw bolt tips
    self.canvas.create_line(r1_x-10, y-85, r1_x+10, y-85,fill='#432702',width=3,tags='rotor')
    self.canvas.create_line(r1_x-10, y+85, r1_x+10, y+85,fill='#432702',width=3,tags='rotor')
    self.canvas.create_line(r2_x-10, y-85, r2_x+10, y-85,fill='#432702',width=3,tags='rotor')
    self.canvas.create_line(r2_x-10, y+85, r2_x+10, y+85,fill='#432702',width=3,tags='rotor')
    self.canvas.create_line(r3_x-10, y-85, r3_x+10, y-85,fill='#432702',width=3,tags='rotor')
    self.canvas.create_line(r3_x-10, y+85, r3_x+10, y+85,fill='#432702',width=3,tags='rotor')
    self.canvas.create_line(r4_x-10, y-85, r4_x+10, y-85,fill='#432702',width=3,tags='rotor')
    self.canvas.create_line(r4_x-10, y+85, r4_x+10, y+85,fill='#432702',width=3,tags='rotor')

    # Draw white boxes
    self.canvas.create_rectangle(r1_x-25, y-25, r1_x+25, y+25,fill='white',width=0,tags='rotor')
    self.canvas.create_rectangle(r2_x-25, y-25, r2_x+25, y+25,fill='white',width=0,tags='rotor')
    self.canvas.create_rectangle(r3_x-25, y-25, r3_x+25, y+25,fill='white',width=0,tags='rotor')
    self.canvas.create_rectangle(r4_x-25, y-25, r4_x+25, y+25,fill='white',width=0,tags='rotor')

    # Draw Text
    self.visible_text=[]
    self.visible_text.append(self.canvas.create_text(r1_x,y,fill="black", font="sans 20",text=chr(self.visible_letters[0]).capitalize(),tags='rotor'))
    self.visible_text.append(self.canvas.create_text(r2_x,y,fill="black", font="sans 20",text=chr(self.visible_letters[1]).capitalize(),tags='rotor'))
    self.visible_text.append(self.canvas.create_text(r3_x,y,fill="black", font="sans 20",text=chr(self.visible_letters[2]).capitalize(),tags='rotor'))
    self.visible_text.append(self.canvas.create_text(r4_x,y,fill="black", font="sans 20",text=chr(self.visible_letters[3]).capitalize(),tags='rotor'))

    self.canvas.update()

  # Switch Pages
  def switch_to(self, page):
    x = 1100
    y = 50
    if (page == 'main'):
      self.current_page = page
      for index, button in enumerate(self.main_buttons):
        button.place(x=x,y=y+index*40)
      for button in self.config_buttons:
        button.place_forget()
    elif (page == 'config'):
      self.current_page = page
      for index, button in enumerate(self.config_buttons):
        button.place(x=x,y=y+index*40)
      for button in self.main_buttons:
        button.place_forget()
    else:
      print("Wrong page input")

# Key board/lamp board functions
# set_key_coords: Creates a list of coordinates for each key. Makes it easier to draw over them later
# draw_key: draws a circle for a key and is turned on or off based on boolean parameter
# draw_keyboard: draws unlit keyboard through use of draw_key method and coords from set_key_coords
  def set_key_coords(self):
    keyboard=['qwertzuio','asdfghjk','pyxcvbnml']
    x_coords=[85,160,85]
    y_coords=[375,500,635]
    gap = 140
    r = 0

    for row in keyboard:
      c = 0
      for key in row:
        self.key_coords.append([x_coords[r]+c*gap,y_coords[r],key])
        c = c + 1
      r = r + 1
    self.key_coords.sort(key = lambda x:x[2])

  # Draw key
  def draw_key(self,x,y,r,key,on):
    if on:
      fill_colour='#e1d87c'
    else:
      fill_colour='#292929'
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    self.canvas.create_oval(x0,y0,x1,y1,fill=fill_colour, outline='black',width=5,tags='key')
    return self.canvas.create_text(x,y,fill="white", font="sans 40 bold", text=key.capitalize(),tags='key')
    

  # Draw keyboard
  def draw_keyboard(self):
    self.keyboard = []
    for key in self.key_coords:
      self.keyboard.append(self.draw_key(key[0],key[1],50,key[2],False))
      

  # Input letter into enigma machine
  def input_letter(self, e):
    if (self.current_page == 'main'):
      if (len(e.char) > 0):
        letter = ord(e.char)
        if(letter >= 97 and letter <= 122):
          self.light_keyboard(self.enigma.enter_key(e.char))
          self.draw_alphabet_ring()

  # Light up lampboard/keyboard
  def light_keyboard(self, key):
    self.canvas.itemconfig(self.keyboard[key], fill='#f2931a')
    self.root.after(500, lambda: self.canvas.itemconfig(self.keyboard[key], fill='#fff'))


# Rotor functions
  def draw_alphabet_ring(self):
    temp = self.enigma.get_visible_letters()
    for i in range(len(temp)):
      if temp[i] != self.visible_letters[i]:
        self.visible_letters[i] = temp[i]
        self.canvas.itemconfig(self.visible_text[i], text=chr(self.visible_letters[i]).capitalize())

  def reset(self):
    self.enigma.reset()
    self.visible_letters = self.enigma.get_visible_letters()
    self.draw_enigma()

  def update_enigma(self):
    new_config = Config(
      [3,1,1],
      [6,1,1],
      [5,1,1],
      [17,1,1],
      1,
      []
    )
    self.enigma.new_config(new_config)
    self.reset()

# Run screen loop
  def run(self):
    self.root.bind('<Key>', self.input_letter)
    self.canvas.pack(side="bottom")
    self.root.mainloop()

# Main Loop
screen = Screen(1280,720,'Enigma Machine - M4 Shark')
screen.run()