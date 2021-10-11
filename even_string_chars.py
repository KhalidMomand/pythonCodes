#!/usrs/bin/env python3

#this program is about, to take input from user and return the characters at even index

#define a function for this task

def even_index_chars(string):
   #first of all, let's store the length of given string to length variable
   length = len(string)
   #now let's iterate through even characters of the given string and display it to the screen
   for char in  range(0, length-1,2):
      print(string[char])


string = str(input('Enter Something: '))
even_index_chars(string)

