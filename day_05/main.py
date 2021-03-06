f = open('input.txt')

line = ' '
nice = nice_2 = 0
while line != '':
  line = f.readline()
  length = len(line)
  double = naughty = False
  vowels = 0

# Part 1
  for i in range(length):
    if ((line[i] == 'a') or (line[i] == 'e') or (line[i] == 'i') or
        (line[i] == 'o') or (line[i] == 'u')):
      vowels += 1
    if line[i] == line[i-1]:
      double = True
    if ((line[i-1] == 'a' and line[i] == 'b') or
        (line[i-1] == 'c' and line[i] == 'd') or
        (line[i-1] == 'p' and line[i] == 'q') or
        (line[i-1] == 'x' and line[i] == 'y')):
      naughty = True
  if (vowels > 2 and double and (not naughty)):
    nice += 1

# Part 2
  pairs = []
  spaced = two_pair = False
  for i in range(0, length-2):
    pairs = pairs + [line[i:i+2]]
    if line[i] == line[i+2]:
      spaced = True
  for i in range(len(pairs)):
    for j in range(i+1, len(pairs)):
      if pairs[i] == pairs[j] and i+1 != j:
        two_pair = True
  if two_pair and spaced:
    nice_2 += 1
  
print("part 1: ", nice)
print("part 2: ", nice_2)

