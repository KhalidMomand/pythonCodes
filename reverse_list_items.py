#!/usrs/bin/env python3

'''
Task :
 write a script to take a list as a parameter from a user and return its reversed version as a result.
 Example: [2, 3, 4, 5] if pass then result will be [5, 4, 3, 2]
'''

#1Solution, Let's write a function 


def reverse_items_list(items_list):

   __reversed_items_list = []
   __original_items_list = items_list
   __reversed_index = len(items_list) - 1

   for index, item in enumerate(items_list):
      __reversed_items_list.append(items_list[__reversed_index-index])
   

   return __reversed_items_list


#Now the function is defined, let's define a function to prompt user to pass a list

def prompt_user_to_pass_items_list():
   items_list = input("Enter Numbers only: " )
   items_list = list(items_list)
   print(reverse_items_list(items_list))



if __name__ == "__main__":
   prompt_user_to_pass_items_list()

