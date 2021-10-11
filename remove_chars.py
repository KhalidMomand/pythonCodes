#!/usrs/bin/env python3

'''
Task: write a program to remove characters from a string from zero up to "n" and return a new 
string. string must be given by user.

'''

#define a function which takes string, and number of characters
def remove_n_char(string, number_of_chars):
   result = string[number_of_chars:]
   return result

#before calling the function, let's prompt user to input the string
string = str(input('Enter String: '))
number_of_chars = int(input('Number of Char:'))

if __name__ == "__main__":
   print(remove_n_char(string,number_of_chars))

