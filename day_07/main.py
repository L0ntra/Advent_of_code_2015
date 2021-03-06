import random, time, __main__, sys
#sys.stdout = open('file.txt', 'w')

class TREE:
  def __init__(self, name):
    self.name = name
    self.left = self.right = None

  def add_leaf(self, leaf):
    if leaf.name < self.name:
      if self.left:
        self.left = self.left.add_leaf(leaf)
      else:
        self.left = leaf
    elif leaf.name > self.name:
      if self.right:
        self.right = self.right.add_leaf(leaf)
      else:
        self.right = leaf
    elif leaf.name == self.name:
      leaf.left = self.left
      leaf.right = self.right
      return leaf
    return self
 
  def print_all(self):
      if self.left:
        self.left.print_all()
      self.print_data()
      if self.right:
        self.right.print_all()
      return None

  def print_data(self):
    print("Name: ", self.name, end = '')

  def search(self, name):
    if name == self.name:
      return self
    if name < self.name and self.left:
      return self.left.search(name)
    elif name > self.name and self.right:
      return self.right.search(name)
    else:
      return None

#OPERATION TYPES
class binary(TREE):
  def __init__(self, name, a, b):
    TREE.__init__(self, name)
    self.a = a
    self.b = b
    None 

  def print_data(self):
    TREE.print_data(self)
    print(" A: ", self.a, "  B: ", self.b)

  def val_a(self, root):
    try:
      return root.search(self.a).ret_value(root)
    except:
      return int(self.a)

  def val_b(self, root):
    try:
      return root.search(self.b).ret_value(root)
    except:
      return int(self.b)

  def p_a(self, root):
    try:
      a = int(self.a)
    except:
      root.search(self.a).p_val(root)
    else:
      print(a, end = '')

  def p_b(self, root):
    try:
      b = int(self.b)
    except:
      root.search(self.b).p_val(root)
    else:
      print(b, end = '')
    

class unary(TREE):
  def __init__(self, name, a, b = None):
    TREE.__init__(self, name)
    self.a = a

  def print_data(self):
    TREE.print_data(self)
    print(" A: ", self.a)

  def val_a(self, root):
    try:
      return root.search(self.a).ret_value(root)
    except:
      return int(self.a)

  def p_a(self, root):
    try:
      a = int(self.a)
    except:
      root.search(self.a).p_val(root)
    else:
      print(a, end = '')


#OPERATIONS
class NOT(unary):
  def ret_value(self, root):
    return (~self.val_a(root)) % 65536

  def p_val(self, root):
    print("~", end = '')
    self.p_a(root)
    return None

class VAL(unary):
  def ret_value(self, root):
    return self.val_a(root)

  def p_val(self, root):
    self.p_a(root)
    return None

class AND(binary):
  def ret_value(self, root):
    return self.val_a(root) & self.val_b(root)

  def p_val(self, root):
    print('(', end = '')
    self.p_a(root)
    print("&", end = '')
    self.p_b(root)
    print(')', end = '')    
    return None

class OR(binary):
  def ret_value(self, root):
    return self.val_a(root) | self.val_b(root)

  def p_val(self, root):  
    print('(', end = '')
    self.p_a(root)
    print("|", end = '')
    self.p_b(root)
    print(')', end = '')
    return None

class XOR(binary):
  def ret_value(self, root):
    return self.val_a(root) ^ self.val_b(root)

  def p_val(self, root):
    print('(', end = '')
    self.p_a(root)
    print("^", end = '')
    self.p_b(root)
    print(')', end = '')
    return None

class LSHIFT(binary):
  def ret_value(self, root):
    val = self.val_a(root) << self.val_b(root)
    if val > 0b1111111111111111:
      print("<<<< ERROR >>>>")
    return val

  def p_val(self, root):
    print('(', end = '')
    self.p_a(root)
    print("<<", end = '')
    self.p_b(root)
    print(')', end = '')
    return None

class RSHIFT(binary):
  def ret_value(self, root):
    return self.val_a(root) >> self.val_b(root)

  def p_val(self, root):
    print('(', end = '')
    self.p_a(root)
    print(">>", end = '')
    self.p_b(root)
    print(')', end = '')
    return None


def piece(line):
  func = name = a = b = None
  space = length = len(line)
  for i in range(length):
    if line[i] == ' ' or line[i] == '\n':
      space = i
      break
  a = line[0:space]
  return a, line[space+1:]

def read_line(line):
  a=b=c=d=e= None
  if line:
    a, line = piece(line)
  if line:
    b, line = piece(line)
  if line:
    c, line = piece(line)
  if line:
    d, line = piece(line)
  if line:
    e, line = piece(line)
  print(a,b,c,d,e)
  if e: #Binary (func, name, a, b)
    return (b, e, a, c)
  elif d: #NOT (func, name, a, None)
    return (a, d, b, None)
  else: #VAl (func, name, a, None)
    return ('VAL', c, a, None)


def new_leaf(params): #params = (func, name, a, b)
  func = getattr(__main__, params[0])
  return func(params[1], params[2], params[3])
"""
root = AND('a', '1', 'b')
root = root.add_leaf(NOT('b', '1'))
root.p_val(root)
print()
root.print_all()
root = root.add_leaf(OR('a', '1', '2'))
print(root.search('a').ret_value(root))
print()
root.print_all()
"""


f = open("input.txt")
root = None
line = f.readline()
root = new_leaf(read_line(line))
line = f.readline()
while line != '':
  root.add_leaf(new_leaf(read_line(line)))
  line = f.readline()
root.print_all()
# root = root.add_leaf(VAL('b', '3176')) ## Remove comment for part 1
for i in range(ord('b'), ord('l')+1):
  for j in range(ord('a'), ord('z')+1):
    root = root.add_leaf(VAL(chr(i)+chr(j), root.search(chr(i)+chr(j)).ret_value(root)))
#print(root.search('a').ret_value(root))

print(root.search('a').ret_value(root))

#root = AND('a', 'b', 'd')
#root.add_leaf(NOT('b', 'c'))
#root.add_leaf(VAL('c', '123')) #5
#root.add_leaf(OR('d', 'b', 'c'))
#root.add_leaf(NOT('e', 'f'))
#root.add_leaf(VAL('f', 0))
#root.add_leaf(RSHIFT('g', 'c', '2'))
#root.add_leaf(LSHIFT('h', 'g', '2'))   
#root.add_leaf(OR('i', '1', '2'))
#root.add_leaf(AND('j', 0b101, 0b111))
#a = OR
#root.add_leaf(a('k', '1', '2'))
#A = B & C   #B = ~C   #C = 101
#A = ~C & C
#A = 010 & 101
#A = 000
#root.print_all()

#for i in range(ord('a'), ord('k')+1):
#  found = root.search(chr(i))
#  if found:
#    print(chr(i), "= ", end = '')    
#    found.p_val(root)
#    print(" =", found.ret_value(root), end = '')
#    print()
#print()

#print(bin((found.ret_value(root))))

