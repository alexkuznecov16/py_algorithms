def get_even_list(user_list: list) -> list:
  result = list() # initial result
  for i in range(len(user_list)):
    if user_list[i] % 2 == 0:
      result.append(user_list[i]) # if list item is even -> append to result
  
  return result

print(get_even_list([1,2,3,4,5,6])) # [2, 4, 6]