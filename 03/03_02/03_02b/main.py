# Key: State
# Value: Capital

states_to_capitals = {
  "Texas":"Austin",
  "Kenya":"Nairobi"
}

print(states_to_capitals["Kenya"])

for key, value in states_to_capitals.items():
  print(f"State: {key} Capital: {value} ")