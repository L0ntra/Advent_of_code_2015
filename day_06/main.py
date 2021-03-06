## x1,y1 through x2,y2 switch = {0 = off, 1 = on, 2 = toggle}
def turn(grid, x1, y1, x2, y2, switch):
  #if switch == 2:
  #  for i in range(x1, x2 + 1):
  #    for j in range(y1, y2 + 1):
  #      if grid[i][j] == 1:
  #        grid[i][j] = 0
  #      else:
  #        grid[i][j] = 1
  #  return None

  for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
      grid[i][j] += switch
      if grid[i][j] < 0:
        grid[i][j] = 0
  return None

#Searches for the next tow numbers nad returns them
def seek(line):
  length = len(line)
  space = length
  for i in range(length):
    if line[i] == ',':
      comma = i
      break
  for i in range(comma, length):
    if line[i] == ' ':
      space = i
      break
  x = int(line[0:comma])
  y = int(line[comma+1:space])
  return(x,y)

def main():
  grid = [[0 for i in range(1000)] for j in range(1000)]
  f = open('input.txt')
  line = ' '
  while line != '':
    line = f.readline()
    if line[:8] == "turn off":
      x1, y1 = seek(line[9:])
      x2, y2 = seek(line[19 + len(str(x1)) + len(str(y1)):])
      turn(grid, x1, y1, x2, y2, -1)
    if line[:7] == "turn on":
      x1, y1 = seek(line[8:])
      x2, y2 = seek(line[18 + len(str(x1)) + len(str(y1)):])
      turn(grid, x1, y1, x2, y2, 1)
    if line[:6] == "toggle":
      x1, y1 = seek(line[7:])
      x2, y2 = seek(line[17 + len(str(x1)) + len(str(y1)):])
      turn(grid, x1, y1, x2, y2, 2)
#    print(line, x1, y1, x2, y2)
#    input()
  part_1 = 0
  for i in range(1000):
    for j in range(1000):
      part_1 += grid[i][j]
  print(part_1)

  return 0

if __name__ == "__main__":
  grid = [[0 for i in range(10)] for j in range(10)]
  turn(grid, 0, 0, 9, 9, 1)
  turn(grid, 0, 0, 5, 5, -1)
  turn(grid, 0, 0, 5, 5, -1)
  turn(grid, 4, 4, 6, 6, 2)
  for i in range(10):
    print(grid[i])
  count = 0
  for i in range(10):
    for j in range(10):
        count += grid[i][j]
  print(count)
   
  
  main()
