# Linear Search

my_list = [6,7,3,15,3,0]
ITEM = 15

def search(item, listy):
  for element in listy:
    if element == item:
      return True
  return False

print(search(ITEM, my_list))
  