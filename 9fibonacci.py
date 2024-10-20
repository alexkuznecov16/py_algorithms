def fibonacci(max: int) -> list:
  if max <= 0:
    return []
  elif max == 1:
    return [0]
  else:
    sequence = [0, 1] # initial sequence
    while (sequence[-1] + sequence[-2] < max):
      sequence.append(sequence[-1] + sequence[-2]) # append to sequence sum of two latest elements
    
    return sequence

print(fibonacci(20)) # [0, 1, 1, 2, 3, 5, 8, 13]
print(fibonacci(1)) # [0]
print(fibonacci(-4)) # []