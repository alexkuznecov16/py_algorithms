def chiper(user_string: str, shift: int) -> str:
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '
  result = []
  for i in range(len(user_string)):
    result.append(letters[(letters.find(user_string[i]) - shift) % len(letters)])
    
  print("".join(result))
    
chiper('Hello my dear friend', 3) # Ebiil7jv7abXo7cofbka
chiper('Hello my dear friend', -3) # KhoorCp1CghduCiulhqg