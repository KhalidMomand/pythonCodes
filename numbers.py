#!/usrs/bin/env python3

#creating a funcation which prints current number , previous number and sum of both numbers in range of 10.

def numberRange(startNumber,RangeNumber):
   print('Printing sum of numbers between required range of numbers along with current and previous number')
   for number in range(startNumber, RangeNumber):
      cNumber = number       #cNumber stands for current Number
      pNumber = cNumber - 1  #pNumber stands for previous number
      pNumher = 0 if pNumber == -1 else pNumber == pNumber   
      sNumber = cNumber + pNumber #sNumber stands for sum of current Number and previous Number
      print('Current Number {} Previous Number {} Sum: {} '.format(cNumber,pNumber,sNumber))


if __name__ == '__main__':
   numberRange(0, 10)


