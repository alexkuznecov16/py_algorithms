def get_max(user_list: list):
  result = -2000000 # initial result
  for i in range(len(user_list)):
    # here we check is it element a nested list
    if type(user_list[i]) is list:
      for t in range(len(user_list[i])):
        if user_list[i][t] > result:
          result = user_list[i][t]
    else:
      if user_list[i] > result:
        result = user_list[i]
        
  return result

print(get_max([18,2,3,4,5,[1,2,3,4,2000]])) # 2000
print(get_max([[1,2], [-1,-2], [7,8], [1, 9], 10, [8, 2]])) # 10
