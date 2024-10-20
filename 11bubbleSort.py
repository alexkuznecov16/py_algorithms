def bubble_sort(user_list: list) -> list:
  # iterate x times -> for correct sorting and check other values to be bigger
  for t in range(len(user_list) - 1):
    # iterate each list element to be bigger than next
    for x in range(len(user_list) - 1):
      if user_list[x] > user_list[x+1]:
        # x+1 smaller than x -> append to x position (bottom)
        # x bigger than x+1 -> append to x+1 position (top)
        
        user_list[x], user_list[x+1] = user_list[x+1], user_list[x] # change positions
  return user_list

print(bubble_sort([0,5,1,4,2])) # [0, 1, 2, 4, 5]
print(bubble_sort([0,2,-2,-4])) # [-4, -2, 0, 2]