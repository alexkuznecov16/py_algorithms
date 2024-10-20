def is_palindrome(user_string: str) -> bool:
  result = False # initial result
  if user_string.lower() == user_string.lower()[::-1]:
    result = True # if string is a palindrome -> set true
  
  return result


print(is_palindrome('Alexander')) # False
print(is_palindrome('Dad')) # True