def is_prime(num: int) -> bool:
  if num == 1:
    return False
  elif num == 2:
    return True
  else:
    # iterate each num between 2 and num (including)
    for i in range(2, num+1):
      if num % i == 0:
        return False
      else:
        return True
    

print(is_prime(11)) # True
print(is_prime(401)) # True
print(is_prime(20)) # False