#!/usrs/bin/env python3

'''
Task ==>
write a function to return True if the first and last number of a given list is same. if numbers are different then return False.

'''
#Let 's first create a function for this task

def is_first_last_item_same(items_list):
   first_item = items_list[0]
   last_item = items_list[-1]
   if first_item == last_item:
      return True
   return False




if __name__ == "__main__":
   print('it returns True cause the first and last items are same.')
   is_first_last_item_same([10, 20, 30, 10])
   print('it returns False cause the first and last item aren\'t matching')
   is_first_last_item_same([20, 30, 40, 50])
