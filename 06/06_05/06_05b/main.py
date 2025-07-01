from collections import deque

def is_there_matching_parentheses(my_text):
  parentheses_stack = deque();
  for char in my_text:
    if char == '(' :
      parentheses_stack.append(char)
    elif char == ')':
      if not parentheses_stack:
        return False
      parentheses_stack.pop()
  return len(parentheses_stack) == 0
    
print(is_there_matching_parentheses("(())(htis(jk))"))   
print(is_there_matching_parentheses("(htis(jk)))"))



