# Tuples are immutable array-like structures

point = (5,2)

x = point[0]
y = point[1]

def calculate_square_properties(side_length):
  area = side_length*side_length
  perimeter = side_length*4

  results = (area, perimeter)
  print(results)

calculate_square_properties(5)
