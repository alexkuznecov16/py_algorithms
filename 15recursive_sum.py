def recursive_sum(num: int):
  # works while num is bigger than 0
  if (num > 0):
    return num + recursive_sum(num-1) # num + latest num
  return num # return result

print(recursive_sum(3)) # 6 -> 3+2+1+0
print(recursive_sum(5)) # 15 -> 5+4+3+2+1+0