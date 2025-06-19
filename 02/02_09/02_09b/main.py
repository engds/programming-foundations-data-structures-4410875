def find_second_smallest(my_list):
    if len(my_list) >=2:
       reverse_sorted_list = sorted(my_list, reverse=True)
       return(my_list[-3])
    return None

print(find_second_smallest([5, 8, 3, 2, 6]))


INPUT_LIST = [9,4,3,10,2,6]

def find_second_smallest_item(listy):
  sorted_list = sorted(listy)
  print(f"The second smallest item is {sorted_list[1]}")


find_second_smallest_item(INPUT_LIST)