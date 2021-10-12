#!/usrs/bin/env python3
'''
Task == > 
write a program to find how many times a substring "Any String that user type" appears in the given string.
'''

#Solution, Let's define a function which takes two strings, Sentence  and substring, we will check  substring in the
# sentence that how many times it appears.


def how_many_times_substring_appears(string, substring):
   if type(string)  and type(substring) == str:
      if substring in string:
         how_many_times = string.count(substring)
         return " '{}' appears '{}' times in the '{}' paragraph. " .format(substring, how_many_times, string)
      else:
         return "The Substring does'nt exist in the given string"
   else:
      return "Only Strings Please"


if __name__ == "__main__":
   string_user_input = str(input("Enter Sentence: "))
   substring_user_input = str(input("Enter Substring: "))
   print(how_many_times_substring_appears(string_user_input,substring_user_input))


