#!/usr/bin/python3

dic = {
       "Name": "Tom",
       "Color": "Red",
       "Number": 1234,
       "Serial": "ASDFd23sasd"
       }

print("Dic to print {}".format(dic))
print("Printing by item in dictionary: ")

for n, (key, val) in enumerate(dic.items()):
    print("{} key {}, contains {}".format(n, key, val))



