def list_max(user_list: list):
  result = user_list[0] # initial result
  for i in range(len(user_list)):
    if user_list[i] > result:
      result = user_list[i] # if list item is bigger than result -> set the result
  
  return result

print(list_max([1,2,3,4,5,6,7])) # 7
print(list_max([-2, -100, 242, 10*70, -722])) # 700