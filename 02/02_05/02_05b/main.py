seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]
#print(seating_chart[2][1])

for i, row in enumerate(seating_chart):
  print(f"row {i+1}, students {row}")

for i, row in enumerate(seating_chart):
  for j, col in enumerate(row):
    print(f"row {i+1},seat {j+1}, {row[j]} or {col}")

