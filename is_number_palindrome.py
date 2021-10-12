#!/usrs/bin/env python3

'''
Task:

write a program to check if the given number is the palindrome number or not.
what is palindrome number? 
if the reversal of number is same is its original then it is called palindrome number
Example : 545 is a palindrome number
'''
#Solution, let's create a function for this purpuse.

def is_number_palindrome(number):
   if type(number) == int:

      __reverse_number = 0
      __original_number = number

      while number > 0:
         reminder = number % 10
         __reverse_number = (__reverse_number  * 10 ) + reminder
         number = number // 10
         


      if __reverse_number  == __original_number:
         return "{} is a palindrome number".format(__original_number)
      else:
          return "{} is not a palindrome number".format(__original_number)


   else:
      return "Please only Integers"


if __name__ == "__main__":
   number_user_input = int(input("Enter Number: "))
   print(is_number_palindrome(number_user_input))


