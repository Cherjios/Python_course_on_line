#!/usr/bin/python3

newList = [1,2,3,4,5,"hola","hello","Rocko"]

print("Element in list {}".format(newList))

for i in newList:
    print("{}".format(i))

print("________________________________________________________")
for i in range(len(newList)): 
    print("{}".format(newList[i]))

print("________________________________________________________")

[print (i) for i in newList]

print("________________________________________________________")
#using enumerates

for i, val in enumerate(newList):
    print("{}, {}".format(i, val))
