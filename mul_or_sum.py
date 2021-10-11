#!/usr/bin/env python3

# define a function, which takes two numbers as arguments, it will check if the multiplication of numbers are grater
# than 1000 then it will return the multiplication result otherwise it will return its sum result
def mul_or_sum(num1, num2):
   #first of all, let's intialize a variable and assign multiplication result of both numbers to the variable
   product = num1 * num2
   #use if condition, to check whether the  multipalication result of both numbers are greater then 1000
   if product > 1000:
      return product
   else:
       product = num1 + num2
       return product

#now, let's excute the  function
if __name__ == "__main__":
   result = mul_or_sum(10, 30)
   print(result)
   
   result2 = mul_or_sum(400 , 300)
   print(result2)


