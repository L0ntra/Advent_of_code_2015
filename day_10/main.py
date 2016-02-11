#number as string
def look_and_say(number):
  length = len(number)
  current = number[0] #the current number being looked at
  output = '' #new string output
  count = 1 #number of times seen
  i = 0
  for i in range(1, length):
    if current != number[i]:
      output += str(count) + current
      current = number[i]
      count = 1
    else:
      count += 1
  output += str(count)+current
  return output

number = '1321131112'
for i in range(50):
#  print(i)
  number = look_and_say(number)
#print(number)
print(len(number))
