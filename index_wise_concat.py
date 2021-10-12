#!/usrs/bin/env python3

'''
Task: 
write a program to concatinate two different lists index - wise, but the list must have the size of items
Example: aList = ["m" , "na", "i", "Kha"] bList = ["y", "me", "s", "lid"] result will be cList = ["my", "name", "is", "khalid"]
'''


#let's define a function for this task


def index_wise_concat(a_list, b_list):
   c_list = []
   for item1, item2 in zip(aList,bList):
      new_item = item1 + item2
      c_list.append(new_item)

   return c_list


# Now let's create two lists
aList = ['m', 'na', 'i', 'kha']
bList = ['y', 'me', 's', 'lid']

# let's excute the program and check if it is working

if __name__ == "__main__":
   print(index_wise_concat(aList,bList))



'''
Another way to solve the issue is as follow

aList= ['m', 'na', 'i', 'kha']
bList = ['y', 'me', 's', 'lid']

cList = [item1 + item2 for item in zip(aList,bList)]


this way of solving the issue is called list comprehenssion

'''
