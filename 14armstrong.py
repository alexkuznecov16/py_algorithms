def is_armstrong(num: int) -> bool:
  num_list = [int(item) for item in str(num)] # iterate each num item to list
  result = 0 # initial result
  
  # iterate each num_list number
  for x in range(0, len(num_list)):
    num_list[x] **= len(num_list) # power num to list length
    result += num_list[x] # powered num add to result
    
  # if the sum of the numbers equals to the initial num -> it's Armstrong number
  if sum(num_list) == num:
    return True
    
  return False
    
print(is_armstrong(456)) # False
print(is_armstrong(153)) # True
print(is_armstrong(1)) # True
print(is_armstrong(0)) # True