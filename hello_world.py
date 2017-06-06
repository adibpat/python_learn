#!/usr/bin/python
import sys

#Simple print
print("Hello, World")

#API to print that takes an argument
def print_hello(who):
    print("hello, {}".format(who))

if __name__ == "__main__":
    print_hello("Sharda")
    print_hello(sys.argv[1])
