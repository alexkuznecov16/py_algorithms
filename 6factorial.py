def factorial(num: int) -> int:
  result = 1 # initial result
  
  # loop working, while num is not equals 0
  while(num != 0):
    result *= num # multiply result to user number
    num -= 1 # minus after multiply
    
  return result

print(factorial(5)) # 120
print(factorial(0)) # 1