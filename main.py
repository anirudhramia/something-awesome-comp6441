from enigma import EnigmaMachine

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

# Rotors
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
enigma = EnigmaMachine(1, [17, 3, 2, 1],True)
#                      Ref, 4, 3, 2, 1

enigma.start()