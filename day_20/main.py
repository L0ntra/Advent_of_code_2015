#still bad

def prime_div(n):
  j = int ((n/2))
  start = 0
  for i in range(2, j+1):
    if n%i == 0:
      r = prime_div(int(n/i))
      for j in range(len(r)):
        r = r + [r[j] * i]
      return r #[i] + prime_div(int(n/i))
  return [n, 1]

def rem_dupes(l):
  le = len(l)
  l2 = []
  for i in range(le):
    if l2.count(l[i]) == 0:
      l2 += [l[i]]
  return l2


n = 34000000
n2 = int(n/2)
#n = 10
l = [0 for i in range(n)]
for i in range(1,n2):
  for j in range(i,i*50,i):
    if j < n:
      l[j] = l[j] + i*11
for i in range(n):
  if l[i] >= n:
    print(i, l[i])
    break



#ANS = 786240
"""
#This will eventually work, but it takes much longer
for i in range(int(n/2)):
  l = []
  l = prime_div(i)
  l = rem_dupes(l)
  if sum(l) > n:
    print(l, sum(l))
    break
"""

