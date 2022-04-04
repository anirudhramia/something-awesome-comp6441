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
# number, position, ring_setting
    config = Config(
      [1,1,1],
      [2,1,1],
      [3,1,1],
      [16,1,1],
      0,
      []
    )
    self.enigma = EnigmaMachine(config)

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
    self.chosen_rotors=[config.rotor4_number,config.rotor3_number, config.rotor2_number, config.rotor1_number]
    self.rotor_positions=[config.rotor4_position,config.rotor3_position, config.rotor2_position, config.rotor1_position]
    self.rotor_ring_settings=[config.rotor4_ring_setting,config.rotor3_ring_setting, config.rotor2_ring_setting, config.rotor1_ring_setting]
    self.rotor_options_circles=[]
    self.rotors_options=[0,0,0,0,0,0,0,0]
    self.fourth_rotor=self.chosen_rotors[0]

    # Save and return to enigma screen
    self.config_buttons.append(Button(self.canvas, text='Save', command=self.update_enigma))
    # Return to Enigma screen without saving config
    self.config_buttons.append(Button(self.canvas, text="Cancel", command=self.draw_enigma))

    # Reset to default view
    self.draw_enigma()

# Screen change functions
  # Screen with configure options
  def draw_configure_screen(self):
    # Clear
    self.canvas.delete('all')
    self.switch_to('config')

    # Coords
    r_x = 100
    r_y = 100

    # Rotor data
    self.rotor_options=[0,0,0,0,0,0,0,0]
    types=['I','II','III','IV','V','VI','VII','VIII','\u03B2','\u03B3']
    for n in self.chosen_rotors:
      if n < 9:
        self.rotor_options[n-1] = 1
    self.fourth_rotor = self.chosen_rotors[0]

    # Rotors
    self.rotor_options_circles=[]
    self.canvas.create_text(r_x,r_y,fill="white", font="sans 20",text='Rotors: ',tags='rotor_option')
    for i, type in enumerate(types):
      x0 = r_x + 100 + i*65 - 25
      x1 = r_x + 100 + i*65 + 25
      y0 = r_y-25
      y1 = r_y+25
      if i > 7:
        x0 = x0+25
        x1 = x1+25
      button = self.canvas.create_oval(x0, y0, x1, y1,fill='#9c9c9c',outline='#a6a6a6',width=5,tags=('rotor_option',type))
      self.canvas.tag_bind(button,'<Button-1>', self.rotor_select)
      self.canvas.tag_bind(button, '<Enter>', self.on_rotor_enter)
      self.canvas.tag_bind(button, '<Leave>', self.on_rotor_leave)
      self.rotor_options_circles.append(button)
      text = self.canvas.create_text(x0+25,y0+25,fill='white', font="sans 15", text=type, tags='rotor_option')
      self.canvas.tag_bind(text, '<Button-1>', self.rotor_select)
      self.canvas.tag_bind(text, '<Enter>', self.on_rotor_enter)
      self.canvas.tag_bind(button, '<Leave>', self.on_rotor_leave)

    self.draw_rotor_options()


  def draw_rotor_options(self):
    for i, rotor in enumerate(self.rotor_options):
      if rotor == 1:
        self.canvas.itemconfig(self.rotor_options_circles[i], fill='#ffb05c', outline='#ffc382')

    self.canvas.itemconfig(self.rotor_options_circles[self.fourth_rotor-8], fill='#ffb05c', outline='#ffc382')

  def rotor_select(self, e):
    if e.x > 170 and e.x < 230:
      if (self.rotor_options[0] != 1):
        self.rotor_options[0] = 1
      else:
        self.rotor_options[0] = 0
    elif e.x > 235 and e.x < 295:
      if (self.rotor_options[1] != 1):
        self.rotor_options[1] = 1
      else:
        self.rotor_options[1] = 0
    elif e.x > 300 and e.x < 360:
      if (self.rotor_options[2] != 1):
        self.rotor_options[2] = 1
      else:
        self.rotor_options[2] = 0
    elif e.x > 365 and e.x < 425:
      if (self.rotor_options[3] != 1):
        self.rotor_options[3] = 1
      else:
        self.rotor_options[3] = 0
    elif e.x > 430 and e.x < 490:
      if (self.rotor_options[4] != 1):
        self.rotor_options[4] = 1
      else:
        self.rotor_options[4] = 0
    elif e.x > 495 and e.x < 555:
      if (self.rotor_options[5] != 1):
        self.rotor_options[5] = 1
      else:
        self.rotor_options[5] = 0
    elif e.x > 560 and e.x < 620:
      if (self.rotor_options[6] != 1):
        self.rotor_options[6] = 1
      else:
        self.rotor_options[6] = 0
    elif e.x > 625 and e.x < 680:
      if (self.rotor_options[7] != 1):
        self.rotor_options[7] = 1
      else:
        self.rotor_options[7] = 0
    elif e.x > 715 and e.x < 775:
      if (self.fourth_rotor != 16):
        self.fourth_rotor = 16
    elif e.x > 780 and e.x < 840:
      if (self.fourth_rotor != 17):
        self.fourth_rotor = 17

    self.draw_rotor_options()

  def on_rotor_leave(self, e):
    if(self.rotor_options[0] == 1):
      self.canvas.itemconfig('I',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('I',fill='#9c9c9c',outline='#a6a6a6')
    if(self.rotor_options[1] == 1):
      self.canvas.itemconfig('II',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('II',fill='#9c9c9c',outline='#a6a6a6')
    if(self.rotor_options[2] == 1):
      self.canvas.itemconfig('III',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('III',fill='#9c9c9c',outline='#a6a6a6')
    if(self.rotor_options[3] == 1):
      self.canvas.itemconfig('IV',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('IV',fill='#9c9c9c',outline='#a6a6a6')
    if(self.rotor_options[4] == 1):
      self.canvas.itemconfig('V',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('V',fill='#9c9c9c',outline='#a6a6a6')
    if(self.rotor_options[5] == 1):
      self.canvas.itemconfig('VI',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('VI',fill='#9c9c9c',outline='#a6a6a6')
    if(self.rotor_options[6] == 1):
      self.canvas.itemconfig('VII',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('VII',fill='#9c9c9c',outline='#a6a6a6')
    if(self.rotor_options[7] == 1):
      self.canvas.itemconfig('VIII',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('VIII',fill='#9c9c9c',outline='#a6a6a6')
    if(self.fourth_rotor == 16):
      self.canvas.itemconfig('\u03B2',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('\u03B2',fill='#9c9c9c',outline='#a6a6a6')
    if(self.fourth_rotor == 17):
      self.canvas.itemconfig('\u03B3',fill='#ffb05c', outline='#ffc382')
    else:
      self.canvas.itemconfig('\u03B3',fill='#9c9c9c',outline='#a6a6a6')

  def on_rotor_enter(self, e):
    if e.x > 170 and e.x < 230:
      self.canvas.itemconfig('I',fill='#ff9582', outline='#ff7259')
    elif e.x > 235 and e.x < 295:
      self.canvas.itemconfig('II',fill='#ff9582', outline='#ff7259')
    elif e.x > 300 and e.x < 360:
      self.canvas.itemconfig('III',fill='#ff9582', outline='#ff7259')
    elif e.x > 365 and e.x < 425:
      self.canvas.itemconfig('IV',fill='#ff9582', outline='#ff7259')
    elif e.x > 430 and e.x < 490:
      self.canvas.itemconfig('V',fill='#ff9582', outline='#ff7259')
    elif e.x > 495 and e.x < 555:
      self.canvas.itemconfig('VI',fill='#ff9582', outline='#ff7259')
    elif e.x > 560 and e.x < 620:
      self.canvas.itemconfig('VII',fill='#ff9582', outline='#ff7259')
    elif e.x > 625 and e.x < 680:
      self.canvas.itemconfig('VIII',fill='#ff9582', outline='#ff7259')
    elif e.x > 715 and e.x < 775:
      self.canvas.itemconfig('\u03B2',fill='#ff9582', outline='#ff7259')
    elif e.x > 780 and e.x < 840:
      self.canvas.itemconfig('\u03B3',fill='#ff9582', outline='#ff7259')
    

  # Screen with enigma machine
  def draw_enigma(self):
    # Clear
    self.canvas.delete('all')
    self.switch_to('main')

    # Coords
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

    # Text
    text = self.enigma.get_rotor_types()
    self.canvas.create_text(r1_x, y-120,fill='#121212',font="sans 20 bold",text=text[0],tags='rotor')
    self.canvas.create_text(r2_x, y-120,fill='#121212',font="sans 20 bold",text=text[1],tags='rotor')
    self.canvas.create_text(r3_x, y-120,fill='#121212',font="sans 20 bold",text=text[2],tags='rotor')
    self.canvas.create_text(r4_x, y-120,fill='#121212',font="sans 20 bold",text=text[3],tags='rotor')

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

# Config functions
  def update_enigma(self):
    rotors_chosen = 0
    for r in self.rotor_options:
      rotors_chosen = rotors_chosen+r
    if (rotors_chosen != 3):
      self.canvas.create_text(640,25,fill="white",font="sans 20",text="Please select three rotors between I and VIII", tags='warning_text')
      self.root.after(5000, lambda: self.canvas.delete('warning_text'))
    else:
      config = Config(
        [3,1,1],
        [6,1,1],
        [5,1,1],
        [17,1,1],
        1,
        []
      )
      self.chosen_rotors=[config.rotor4_number,config.rotor3_number, config.rotor2_number, config.rotor1_number]
      self.rotor_positions=[config.rotor4_position,config.rotor3_position, config.rotor2_position, config.rotor1_position]
      self.rotor_ring_settings=[config.rotor4_ring_setting,config.rotor3_ring_setting, config.rotor2_ring_setting, config.rotor1_ring_setting]
      self.enigma.new_config(config)
      self.reset()

  def draw_rotor(self):
    print('text')

# Run screen loop
  def run(self):
    self.root.bind('<Key>', self.input_letter)
    self.canvas.pack(side="bottom")
    self.root.mainloop()

# Main Loop
screen = Screen(1280,720,'Enigma Machine - M4 Shark')
screen.run()