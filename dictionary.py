#!/usr/bin/python3

emptyvar = {}

emptyvar[25] = "Square of 5"
emptyvar[2] = "Square of 2"
emptyvar[9] = "Square of 3"

print("dictionary :  {}".format(emptyvar))

newdic = {}

newdic["A"] = 1
newdic["B"] = 2
newdic["C"] = 3

print("dictionary newdic:  {}".format(newdic))

inputKeyToDelete = input("Enter the key you wish to delete from dictionary \n")

if inputKeyToDelete in newdic:
    del newdic[inputKeyToDelete]
    print("elemente deleted from the dictionary {} dic {}".format(inputKeyToDelete, newdic))
print("element {} no present in dic: {} ".format(inputKeyToDelete, newdic))
