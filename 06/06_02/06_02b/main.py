card_stack = []

card_stack.append("JH")
card_stack.append("2D")
card_stack.append("10S")

# front(bottom) ---- back(top)
top_card = card_stack.pop()
print(top_card)


if not card_stack:
  print("Card stack is empty")
else:
  print(f"Stack length is {len(card_stack)} and the top card is {card_stack[-1]}")