#!/usr/bin/env python3

#evenIndex function is used to return characters of a string in even indexes

def evenIndex(string):
   for char in range(0, len(string), 2):
      print(string[char])

if __name__ == "__main__":
   evenIndex('pynative')


