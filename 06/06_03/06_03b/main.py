from collections import deque

history_stack = deque()
history_stack.append("https://google.com")
history_stack.append("https://linkedin.com")
history_stack.append("https://stackoverflow.com")

while len(history_stack) != 0:
  print(history_stack.pop())