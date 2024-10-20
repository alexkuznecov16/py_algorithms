import math, random # import math for floor random numbers

def matrix(num: int):
  matrix = '' # initial matrix
  for i in range(num):
    row = '' # initial matrix row
    for t in range(num):
      row += str(math.floor(random.randint(1, 9))) # add to row (t - count) numbers
      row += ' ' # add space between
    row += '\n' # add new line
    matrix += row # add row to matrix
  return matrix

print(matrix(2))
# 8 4 
# 4 2 

print(matrix(5))
# 2 4 1 8 8 
# 8 8 5 2 5 
# 2 9 4 3 8 
# 4 5 9 6 5 
# 8 6 9 4 9 