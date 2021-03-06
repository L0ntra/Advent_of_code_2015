class deer:
  def __init__(self, name, speed, dash, rest):
    self.name = name
    self.speed = speed
    self.dash = dash
    self.rest = rest
    self.points = 0
    return

  def ret_val(self):
    return self.name, self.speed, self.dash, self.rest


def race(time, speed, dash, rest):
  clock = dist = stam = 0
  while clock < time:
    clock += 1
    dist += speed
    stam += 1
    if stam == dash:
      stam = 0
      clock += rest
  return dist

#2503 seconds

reigndeer = [deer('Vixen', 8, 8, 53),
            deer('Blitzen', 13, 4, 49),
            deer('Rudolph', 20, 7, 132),
            deer('Cupid', 12, 4, 43),
            deer('Donner', 9, 5, 38),
            deer('Dasher', 10, 4, 37),
            deer('Comet', 3, 37, 76),
            deer('Prancer', 9, 12, 97),
            deer('Dancer', 37, 1, 36)]

winner = ''
distance = 0
for time in range(2503):
  for i in range(len(reigndeer)):
    name, speed, dash, rest = reigndeer[i].ret_val()
    temp = race(time, speed, dash, rest)
    if temp > distance:
      winner = name
      distance = temp
  for i in range(len(reigndeer)):
    if reigndeer[i].name == winner:
      reigndeer[i].points += 1
  distance = 0
  winner = ''

points = 0
for i in range(len(reigndeer)):
  if reigndeer[i].points > points:
    points = reigndeer[i].points
    winner = reigndeer[i].name

print(winner, points)

