convert_string = 'FSOKANUERHMBTIYCWLQPZXVGJD'

# Converts the given string of characters into a wiring dictionary that I can use in the rotor and reflector class.
# Purely wrote this so I didnt have to manually type out all the connections
print('[', end='')
for i in range(len(convert_string)):
  print('(', end='')
  print(i,end='')
  print(',',end='')
  print(ord(convert_string[i].lower())-97, end='')
  print(')',end='')
  if(i != len(convert_string)-1):
    print(', ',end='')

print(']',end='')