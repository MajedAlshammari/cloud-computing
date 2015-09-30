i = 0

print("************************* Part 1 *****************************")
aList = ['Oxo', 'OXO', '123454321', 'ROTATOR', '12345 54321']

for i in range(len(aList)):
  name = reversed(aList[i])
  if list(name) == list(aList[i]):
    print("True ", aList[i])
  else:
      print("False", aList[i])






print("************************* Part 2 *****************************")
inPut = input("Enter a String: ")
rev = reversed(inPut)
if list(inPut) == list(rev):
   print("True ", inPut)
else:
   print("False", inPut)