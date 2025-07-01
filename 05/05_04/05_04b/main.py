from collections import deque

# 1
# 10
# 11
# 100
# 101
# 110
# 111
# 1000

# This was quite a challenge! I will need to review

def print_binary_numbers(n):
  if n <= 0:
    return
  
  queue = deque()
  queue.append(1)
  for i in range(n):
    binary=queue.popleft()
    print(binary)
    queue.append(binary*10)
    queue.append(binary*10+1)

print_binary_numbers(8)



  
