#!/usrs/bin/env python3

#write a program to remove characters from a string starting from zero up to n and return a new string

def stringCut(string, removePart):
   if removePart < 0:
      print('Positive Integer Please')
   else:
      newString =string[removePart:]
      print(newString)

if __name__ == "__main__":
   stringCut('pynative', 4)

