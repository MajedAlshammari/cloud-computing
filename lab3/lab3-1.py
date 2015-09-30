
nameList = ['Oxo', 'OXO']

inPut = input("Enter a string: ")

name = reversed("oxx")
rev = reversed(inPut)


print(name)
if list(inPut) == list(rev):
   print("True ")
else:
   print("False")