#!/usr/bin/python
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
    
