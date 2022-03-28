original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
converted = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'


print('{', end='')
for i in range(len(original)):
  print(i,end='')
  print(':',end='')
  print(ord(converted[i].lower())-97, end='')
  if(i != len(converted)-1):
    print(', ',end='')

print('}',end='')