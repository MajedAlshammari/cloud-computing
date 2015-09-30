i = 0

myList = [0] * 5

for i in range(5):
  myList[i] = i

  i = 0
  for i in range(4):
      t = myList[i] + myList[i-1]
      print(t)