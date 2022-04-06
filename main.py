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

    config = Config(
      [1,1,1],
      [2,1,1],
      [3,1,1],
      [16,1,1],
      32,
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
    self.plugboard_buttons = []

    ### Main
    # Configure Button
    self.main_buttons.append(Button(self.canvas, text="Rotor Settings", font='sans',activebackground='#6b6b6b', bg='#bfbfbf', command=self.draw_rotor_screen))

    # Plugboards Config button
    self.main_buttons.append(Button(self.canvas, text="Plugboard Settings", font='sans',activebackground='#6b6b6b', bg='#bfbfbf', command=self.draw_plugboard_screen))

    # Reset Button
    self.main_buttons.append(Button(self.canvas, text="Reset", font='sans', activebackground='#6b6b6b', bg='#bfbfbf', command=self.reset))

    ### Config
    self.chosen_rotors=[config.reflector, config.rotor4_number,config.rotor3_number, config.rotor2_number, config.rotor1_number]
    self.rotor_positions=[config.rotor4_position,config.rotor3_position, config.rotor2_position, config.rotor1_position]
    self.rotor_ring_settings=[config.rotor4_ring_setting,config.rotor3_ring_setting, config.rotor2_ring_setting, config.rotor1_ring_setting]
    

    # Rotor settings
    self.rotor_options = []
    self.rotor_position_options = []
    self.rotor_ring_setting_options = []
    self.rotor_options_text=[]
    self.position_options_text=[]
    self.ring_setting_options_text=[]
    self.types=['I','II','III','IV','V','VI','VII','VIII','\u03B2','\u03B3','UKW-B', 'UKW-C']

    # Arrows for rotor settings
    self.rotor_arrows_up=[]
    self.rotor_arrows_down=[]
    self.position_arrows_up=[]
    self.position_arrows_down=[]
    self.ring_setting_arrows_up=[]
    self.ring_setting_arrows_down=[]

    # Save and return to enigma screen
    self.config_buttons.append(Button(self.canvas, text='Save', font='sans', activebackground='#6b6b6b', bg='#bfbfbf', command=self.update_rotors))
    # Return to Enigma screen without saving config
    cancel = Button(self.canvas, text="Cancel", font='sans', activebackground='#6b6b6b', bg='#bfbfbf', command=self.draw_enigma)
    self.config_buttons.append(cancel)

    ### Plugboard
    # Save and return to enigma screen
    self.plugboard_buttons.append(Button(self.canvas, text='Save and Return', font='sans', activebackground='#6b6b6b', bg='#bfbfbf', command=self.update_plugboard))

    # Plugboard settings
    self.plugboard_settings=config.plugboard
    self.new_plugboard_settings = []
    self.plugpoints = []
    self.plugpoint_pairs = []
    self.plugpoint_colours=['#292929','#292929','#292929','#292929','#292929',
                            '#292929','#292929','#292929','#292929','#292929',
                            '#292929','#292929','#292929','#292929','#292929',
                            '#292929','#292929','#292929','#292929','#292929',
                            '#292929','#292929','#292929','#292929','#292929','#292929']
    self.available_colours=['#ff0000','#ff8800','#ffff00','#00ff00','#0000ff','#6600ff','#ff00ff','#ffffff','#00ffff','#3a7d00','#ffaaff','#2bc3ff','#9eff4a']
    self.used_colours=[]
    self.current_plug = ''

    # Reset to default view
    self.draw_enigma()

# Screen change functions
  #############################################
  # Screen with rotor options                 #
  #                                           #
  # ###########################################
  def draw_rotor_screen(self):
    # Clear
    self.canvas.delete('all')
    self.switch_to('config')

    # Coords
    r_x = 200
    r_y = 150

    # Rotor data
    text=['Reflector', 'Rotor 1', 'Rotor 2','Rotor 3', 'Rotor 4']
    self.rotor_options=[]
    self.rotor_position_options = []
    self.rotor_ring_setting_options = []
    for i,r in enumerate(self.chosen_rotors):
      if r <= 8:
        self.rotor_options.append(r-1)
        if i > 0:
          self.rotor_position_options.append(self.rotor_positions[i-1])
          self.rotor_ring_setting_options.append(self.rotor_ring_settings[i-1])
      elif r > 8 and r < 32:
        self.rotor_options.append(r-8)
        if i > 0:
          self.rotor_position_options.append(self.rotor_positions[i-1])
          self.rotor_ring_setting_options.append(self.rotor_ring_settings[i-1])
      else:
        self.rotor_options.append(r-22)
    
    self.rotor_options_text=[]
    self.rotor_arrows_up=[]
    self.rotor_arrows_down=[]
    self.position_options_text=[]
    self.position_arrows_up=[]
    self.position_arrows_down=[]
    self.ring_setting_options_text=[]
    self.ring_setting_arrows_up=[]
    self.ring_setting_arrows_down=[]

    # Option Headings
    self.canvas.create_text(80,r_y,fill="white", font="sans 20",text='Rotors:',tags='rotor_option')
    self.canvas.create_text(180,r_y+225,fill="white", font="sans 20",text='Position:',tags='rotor_option')
    self.canvas.create_text(150,r_y+450,fill="white", font="sans 20",text='Ring Setting:',tags='rotor_option')

    # Rotors
    for i, type in enumerate(self.rotor_options):
      radius = 40
      gap = 150
      y_gap = 225
      x0 = r_x + i*gap - radius
      x1 = r_x + i*gap + radius
      y0 = r_y-radius
      y1 = r_y+radius

      if i > 0:
        font = "sans 25"
      else:
        font = "sans 15"

      # Circles with rotor numbers
      self.canvas.create_oval(x0, y0, x1, y1,fill='#9c9c9c',outline='#a6a6a6',width=5,tags=('rotor_option',type))

      if i > 0:
        # Squares for position
        self.canvas.create_polygon([x0, y0+y_gap, x1, y0+y_gap, x1, y1+y_gap, x0, y1+y_gap],fill='#9c9c9c',outline='#a6a6a6',width=5,tags=('rotor_option',type))

        # Squares for ring setting
        self.canvas.create_polygon([x0, y0+(y_gap*2), x1, y0+(y_gap*2), x1, y1+(y_gap*2), x0, y1+(y_gap*2)],fill='#9c9c9c',outline='#a6a6a6',width=5,tags=('rotor_option',type))

      # Headings
      self.canvas.create_text(x0+radius,r_y-125,fill="white", font="sans 10",text=text[i],tags='rotor_option')

      # Related text
      rotor_text = self.canvas.create_text(x0+radius,y0+radius,fill='white', font=font, text=self.types[type], tags='rotor_option')
      self.rotor_options_text.append(rotor_text)
      
      if i > 0:
        position_text= self.canvas.create_text(x0+radius,y0+radius+y_gap,fill='white', font=font, text=str(self.rotor_position_options[i-1]), tags='rotor_option')
        self.position_options_text.append(position_text)

        ring_setting_text= self.canvas.create_text(x0+radius,y0+radius+y_gap+y_gap,fill='white', font=font, text=str(self.rotor_ring_setting_options[i-1]), tags='rotor_option')
        self.ring_setting_options_text.append(ring_setting_text)
      

      # Arrows to change rotors
      arrow = self.canvas.create_polygon([x0+radius, r_y-90, x0+radius/2, r_y-65,x0+radius*1.5,r_y-65],fill='#700000',outline='#700000', width=5,tags='rotor_option')
      self.rotor_arrows_up.append(arrow)
      self.canvas.tag_bind(arrow, '<Button-1>', lambda e, i=i, direction=1: self.on_rotor_button_press(i,direction))
      self.canvas.tag_bind(arrow, '<Enter>', lambda e,i=i, arrows=self.rotor_arrows_up: self.on_button_enter(i, arrows))
      self.canvas.tag_bind(arrow, '<Leave>', lambda e,i=i, arrows=self.rotor_arrows_up: self.on_button_leave(i, arrows))

      arrow = self.canvas.create_polygon([x0+radius, r_y+90, x0+radius/2, r_y+65,x0+radius*1.5,r_y+65],fill='#700000',outline='#700000', width=5,tags='rotor_option')
      self.rotor_arrows_down.append(arrow)
      self.canvas.tag_bind(arrow, '<Button-1>', lambda e,i=i, direction=-1: self.on_rotor_button_press(i,direction))
      self.canvas.tag_bind(arrow, '<Enter>', lambda e,i=i, arrows=self.rotor_arrows_down: self.on_button_enter(i, arrows))
      self.canvas.tag_bind(arrow, '<Leave>', lambda e,i=i, arrows=self.rotor_arrows_down: self.on_button_leave(i, arrows))

      if i > 0:
        # Arrows to change position
        arrow = self.canvas.create_polygon([x0+radius, r_y+y_gap-90, x0+radius/2, r_y+y_gap-65,x0+radius*1.5,r_y+y_gap-65],fill='#700000',outline='#700000', width=5,tags='rotor_option')
        self.position_arrows_up.append(arrow)
        self.canvas.tag_bind(arrow, '<Button-1>', lambda e, i=i-1, direction=1: self.on_position_button_press(i,direction))
        self.canvas.tag_bind(arrow, '<Enter>', lambda e,i=i-1, arrows=self.position_arrows_up: self.on_button_enter(i, arrows))
        self.canvas.tag_bind(arrow, '<Leave>', lambda e,i=i-1, arrows=self.position_arrows_up: self.on_button_leave(i, arrows))

        arrow = self.canvas.create_polygon([x0+radius, r_y+y_gap+90, x0+radius/2, r_y+y_gap+65,x0+radius*1.5,r_y+y_gap+65],fill='#700000',outline='#700000', width=5,tags='rotor_option')
        self.position_arrows_down.append(arrow)
        self.canvas.tag_bind(arrow, '<Button-1>', lambda e,i=i-1, direction=-1: self.on_position_button_press(i,direction))
        self.canvas.tag_bind(arrow, '<Enter>', lambda e,i=i-1, arrows=self.position_arrows_down: self.on_button_enter(i, arrows))
        self.canvas.tag_bind(arrow, '<Leave>', lambda e,i=i-1, arrows=self.position_arrows_down: self.on_button_leave(i, arrows))

        # Arrows to change ring_setting
        arrow = self.canvas.create_polygon([x0+radius, r_y+y_gap+y_gap-90, x0+radius/2, r_y+y_gap+y_gap-65,x0+radius*1.5,r_y+y_gap+y_gap-65],fill='#700000',outline='#700000', width=5,tags='rotor_option')
        self.ring_setting_arrows_up.append(arrow)
        self.canvas.tag_bind(arrow, '<Button-1>', lambda e, i=i-1, direction=1: self.on_ring_setting_button_press(i,direction))
        self.canvas.tag_bind(arrow, '<Enter>', lambda e,i=i-1, arrows=self.ring_setting_arrows_up: self.on_button_enter(i, arrows))
        self.canvas.tag_bind(arrow, '<Leave>', lambda e,i=i-1, arrows=self.ring_setting_arrows_up: self.on_button_leave(i, arrows))

        arrow = self.canvas.create_polygon([x0+radius, r_y+y_gap+y_gap+90, x0+radius/2, r_y+y_gap+y_gap+65,x0+radius*1.5,r_y+y_gap+y_gap+65],fill='#700000',outline='#700000', width=5,tags='rotor_option')
        self.ring_setting_arrows_down.append(arrow)
        self.canvas.tag_bind(arrow, '<Button-1>', lambda e,i=i-1, direction=-1: self.on_ring_setting_button_press(i,direction))
        self.canvas.tag_bind(arrow, '<Enter>', lambda e,i=i-1, arrows=self.ring_setting_arrows_down: self.on_button_enter(i, arrows))
        self.canvas.tag_bind(arrow, '<Leave>', lambda e,i=i-1, arrows=self.ring_setting_arrows_down: self.on_button_leave(i, arrows))

  def on_rotor_button_press(self, i, direction):
    if (i >= 2 and i <=4):
      self.rotor_options[i] = self.rotor_options[i] + direction
      if (self.rotor_options[i] > 7):
        self.rotor_options[i] = 0
      if(self.rotor_options[i] < 0):
        self.rotor_options[i] = 7
    elif (i == 1):
      if (self.rotor_options[i] == 8):
        self.rotor_options[i] = 9
      else: 
        self.rotor_options[i] = 8
    elif (i == 0):
      if (self.rotor_options[i] == 10):
        self.rotor_options[i] = 11
      else: 
        self.rotor_options[i] = 10
    else:
      print("Something Wrong!")
    self.canvas.itemconfig(self.rotor_options_text[i], text=self.types[self.rotor_options[i]])

  def on_position_button_press(self, i, direction):
    self.rotor_position_options[i] = self.rotor_position_options[i] + direction
    if (self.rotor_position_options[i] > 26):
      self.rotor_position_options[i] = 1
    elif (self.rotor_position_options[i] < 1):
      self.rotor_position_options[i] = 26
    self.canvas.itemconfig(self.position_options_text[i], text=self.rotor_position_options[i])

  def on_ring_setting_button_press(self, i, direction):
    self.rotor_ring_setting_options[i] = self.rotor_ring_setting_options[i] + direction
    if (self.rotor_ring_setting_options[i] > 26):
      self.rotor_ring_setting_options[i] = 1
    elif (self.rotor_ring_setting_options[i] < 1):
      self.rotor_ring_setting_options[i] = 26
    self.canvas.itemconfig(self.ring_setting_options_text[i], text=self.rotor_ring_setting_options[i])

  def on_button_enter(self, i, arrows):
    self.canvas.itemconfig(arrows[i], fill='#960000', outline='#960000')

  def on_button_leave(self, i,arrows):
    self.canvas.itemconfig(arrows[i], fill='#700000', outline='#700000')

  #############################################
  # Screen with plugboard settings            #
  #                                           #
  # ###########################################

  def draw_plugboard_screen(self):
    self.canvas.delete('all')
    self.switch_to('plugboard')
    self.new_plugboard_settings = self.plugboard_settings
    self.canvas.create_text(300,30,fill='white', font='sans 20', text='Select two letters to connect them')
    self.canvas.create_text(385,60,fill='white', font='sans 20', text='Click an already created connection to remove it')
    self.draw_keyboard()

  def draw_plugpoint(self,x,y,r,key):
    fill_colour=self.plugpoint_colours[ord(key)-97]
    if fill_colour == '#292929':
      outline_colour = 'black'
    else:
      outline_colour = fill_colour
    y = y-125
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r

    y2 = y + 2*r
    y3 = y + 2* + 2*r

    pad=10

    plug = self.canvas.create_polygon([x0-pad,y0-pad,x1+pad,y0-pad,x1+pad,y3+pad,x0-pad,y3+pad],fill=fill_colour,outline=fill_colour, width=15)
    self.canvas.tag_bind(plug, '<Button-1>', lambda e, key=key: self.on_plug_select(key))

    upper_plug = self.canvas.create_oval(x0,y0,x1,y1,fill=fill_colour, outline=outline_colour,width=5,tags='plugpoint')
    self.canvas.tag_bind(upper_plug, '<Button-1>', lambda e, key=key: self.on_plug_select(key))

    lower_plug = self.canvas.create_oval(x0,y2,x1,y3,fill=fill_colour, outline=outline_colour,width=5,tags='plugpoint')
    self.canvas.tag_bind(lower_plug, '<Button-1>', lambda e, key=key: self.on_plug_select(key))
    self.plugpoint_pairs.append([upper_plug, lower_plug])

    self.canvas.create_text(x,y-55,fill="white", font="sans 30 bold", text=key.capitalize(),tags='key')
    return plug

  def on_plug_select(self, key):
    colour='#292929'
    key_found = False
    index_1 = 0
    index_2 = 0
    letter_1 = 0
    letter_2 = 0
    for i,pair in enumerate(self.new_plugboard_settings):
      if (pair[0] == ord(key)-97):
        index_1 = i
        letter_1 = pair[0]
        key_found = True
      elif(pair[1] == ord(key)-97):
        index_2 = i
        letter_2 = pair[0]
        key_found = True

    if(not key_found):
      if (self.current_plug == key):
        self.canvas.itemconfig(self.plugpoints[ord(self.current_plug)-97], fill=colour,outline=colour)
        self.current_plug = ''
      elif (self.current_plug == ''):
        self.current_plug = key
        self.canvas.itemconfig(self.plugpoints[ord(self.current_plug)-97], fill='grey',outline='grey')
      else:
        colour = self.available_colours[0]

        self.canvas.itemconfig(self.plugpoints[ord(key)-97], fill=colour,outline=colour)
        self.canvas.itemconfig(self.plugpoints[ord(self.current_plug)-97], fill=colour,outline=colour)
        self.canvas.itemconfig(self.plugpoint_pairs[ord(key)-97][0], fill=colour,outline=colour)
        self.canvas.itemconfig(self.plugpoint_pairs[ord(key)-97][1], fill=colour,outline=colour)
        self.canvas.itemconfig(self.plugpoint_pairs[ord(self.current_plug)-97][0], fill=colour,outline=colour)
        self.canvas.itemconfig(self.plugpoint_pairs[ord(self.current_plug)-97][1], fill=colour,outline=colour)

        self.plugpoint_colours[ord(key)-97] = colour
        self.plugpoint_colours[ord(self.current_plug)-97] = colour

        c = self.available_colours.pop(0)
        self.used_colours.append(c)

        self.new_plugboard_settings.append([ord(self.current_plug)-97, ord(key)-97])
        self.new_plugboard_settings.append([ord(key)-97, ord(self.current_plug)-97])
        self.current_plug = ''
    else:
      if(index_1 > index_2):
        self.new_plugboard_settings.pop(index_1)
        self.new_plugboard_settings.pop(index_2)
      else:
        self.new_plugboard_settings.pop(index_2)
        self.new_plugboard_settings.pop(index_1)
      if(self.current_plug != ''):
        self.canvas.itemconfig(self.plugpoints[ord(self.current_plug)-97], fill=colour,outline=colour)
        self.current_plug = ''
      c = self.canvas.itemcget(self.plugpoints[letter_2], 'fill')
      self.used_colours.remove(c)
      self.available_colours.append(c)
      self.canvas.itemconfig(self.plugpoints[letter_1], fill=colour,outline=colour)
      self.canvas.itemconfig(self.plugpoints[letter_2], fill=colour,outline=colour)
      self.canvas.itemconfig(self.plugpoint_pairs[letter_1][0], fill=colour,outline='black')
      self.canvas.itemconfig(self.plugpoint_pairs[letter_1][1], fill=colour,outline='black')
      self.canvas.itemconfig(self.plugpoint_pairs[letter_2][0], fill=colour,outline='black')
      self.canvas.itemconfig(self.plugpoint_pairs[letter_2][1], fill=colour,outline='black')
      self.plugpoint_colours[letter_1] = colour
      self.plugpoint_colours[letter_2] = colour


  #############################################
  # Screen with enigma machine                #
  #                                           #
  # ###########################################
  def draw_enigma(self):
    # Clear
    self.canvas.delete('all')
    self.switch_to('main')
    self.enigma.reset()
    self.visible_letters = self.enigma.get_visible_letters()

    # Coords
    r0_x = 60
    r1_x = 190
    r2_x = 340
    r3_x = 490
    r4_x = 640
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
    reflector = self.enigma.get_reflector()
    self.canvas.create_text(r0_x, y-30,fill='white',font="sans 15 bold",text='Reflector:',tags='rotor')
    self.canvas.create_text(r0_x, y,fill='white',font="sans 20 bold",text=reflector,tags='rotor')
    self.canvas.create_text(r1_x, y-120,fill='white',font="sans 20 bold",text=text[0],tags='rotor')
    self.canvas.create_text(r2_x, y-120,fill='white',font="sans 20 bold",text=text[1],tags='rotor')
    self.canvas.create_text(r3_x, y-120,fill='white',font="sans 20 bold",text=text[2],tags='rotor')
    self.canvas.create_text(r4_x, y-120,fill='white',font="sans 20 bold",text=text[3],tags='rotor')

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
      for button in self.plugboard_buttons:
        button.place_forget()
    elif (page == 'config'):
      self.current_page = page
      for index, button in enumerate(self.config_buttons):
        button.place(x=x,y=y+index*40)
      for button in self.main_buttons:
        button.place_forget()
    elif (page =='plugboard'):
      self.current_page = page
      for index, button in enumerate(self.plugboard_buttons):
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
    self.plugpoints = []
    self.plugpoint_pairs = []
    if(self.current_page =='main'):
      for key in self.key_coords:
        self.keyboard.append(self.draw_key(key[0],key[1],50,key[2],False))
    elif(self.current_page == 'plugboard'):
      for key in self.key_coords:
        self.plugpoints.append(self.draw_plugpoint(key[0],key[1],15,key[2]))

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
    self.root.unbind('<Key>')
    self.root.after(500, lambda: [self.canvas.itemconfig(self.keyboard[key], fill='#fff'), self.root.bind('<Key>', self.input_letter)])



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
  def update_rotors(self):
    config = Config(
      [self.rotor_options[4]+1,self.rotor_position_options[3],self.rotor_ring_setting_options[3]],
      [self.rotor_options[3]+1,self.rotor_position_options[2],self.rotor_ring_setting_options[2]],
      [self.rotor_options[2]+1,self.rotor_position_options[1],self.rotor_ring_setting_options[1]],
      [self.rotor_options[1]+8,self.rotor_position_options[0],self.rotor_ring_setting_options[0]],
      self.rotor_options[0]+22,
      self.plugboard_settings
    )
    self.chosen_rotors=[config.reflector, config.rotor4_number,config.rotor3_number, config.rotor2_number, config.rotor1_number]
    self.rotor_positions=[config.rotor4_position,config.rotor3_position, config.rotor2_position, config.rotor1_position]
    self.rotor_ring_settings=[config.rotor4_ring_setting,config.rotor3_ring_setting, config.rotor2_ring_setting, config.rotor1_ring_setting]
    self.enigma.new_config(config)
    self.reset()

# Plugboard functions
  def update_plugboard(self):
    config = Config(
      [self.chosen_rotors[4],self.rotor_positions[3],self.rotor_ring_settings[3]],
      [self.chosen_rotors[3],self.rotor_positions[2],self.rotor_ring_settings[2]],
      [self.chosen_rotors[2],self.rotor_positions[1],self.rotor_ring_settings[1]],
      [self.chosen_rotors[1],self.rotor_positions[0],self.rotor_ring_settings[0]],
      self.chosen_rotors[0],
      self.new_plugboard_settings
    )
    self.plugboard_settings = self.new_plugboard_settings.copy()
    self.enigma.new_config(config)
    self.reset()

# Run screen loop
  def run(self):
    self.root.bind('<Key>', self.input_letter)
    self.canvas.pack(side="bottom")
    self.root.mainloop()

# Main Loop
screen = Screen(1280,720,'Enigma Machine - M4 Shark')
screen.run()