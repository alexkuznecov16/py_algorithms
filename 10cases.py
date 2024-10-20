def to_title_case(user_string: str) -> list:
  result = user_string.split() # string convert to list (each word at a specific index)
  for i in range(len(result)):
    result[i] = result[i].capitalize() # capitalize each word
    
  return ' '.join(result)

print(to_title_case('hello to everyone!')) # Hello To Everyone!
print(to_title_case('i am seventeen')) # I Am Seventeen