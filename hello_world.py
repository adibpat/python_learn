#!/usr/bin/env python3
import sys

#Simple print
print("Hello, World")

#API to print that takes an argument
def print_hello(who):
    print("hello, {}".format(who))

# int, float, null and bool are basic data types in python


if __name__ == "__main__":

    print_hello(sys.argv[1])

    print(0x10) #16 
    print(0b10) #2
    print(0o10) #8
    print(int(-4.4999)) #-4
    print(type(3.45)) #float

#None    
    a = None
    print("a is none = {}".format(a is None)) #True)

#Bool    
    print("bool(0) is {}".format(bool(0))) #False
    print("bool(25) is {}".format(bool(25))) #True
    print("bool(-1) is {}".format(bool(-1))) #True? yes
    print("bool(0.25) is {}".format(bool(0.25))) #True
    print("bool([]) is {}".format(bool([]))) #False
    print("bool([1,2,3]) is {}".format(bool([1,2,3]))) #False        

    rs = r'This is a raw string C:/MyDocuments/projects/blah-blah'
    print(rs)
