import math, random

# gameplay function - to play
def game():
  print('Welcome!\nIt is my game named "Guess random number".') # greetings
  user_name = str(input("What's your name: ")) # get user name
  print(f'{user_name}, you have 3 attempts to enter correct number.') # announcement
  
  # game variables
  guessed_num = math.floor(random.randint(1, 10)) # random number between [1, 10]
  attempts = 0 # initial attempts counter
  isGuessed = False # initial is guessed boolean
  
  # game loop - while attempts counter smaller than 3
  while(attempts < 3):
    attempts += 1 # add 1 to attempts after user guess
    print('Enter number between 1 and 10') # repeat message
    user_guess = int(input('Number: ')) # user guessed num
    
    # checking
    if user_guess == guessed_num:
      isGuessed = True # set true for result
      break # end loop
    else:
      print(f"It's not {user_guess}\n") # not true number
  return attempts, isGuessed, guessed_num, user_name

# result show
def result(attempts: int, isGuessed: bool, guessed_num: int, user_name: str):
  if isGuessed:
    print(f"\nWell done, {user_name}! You won after {attempts} attempts.") # if won
  else:
    print(f"\n{user_name}, you lost! Guessed number was {guessed_num}") # if lost
    
  return True
  
gameplay = game() # get variables from game and set it to result arguments

result(attempts=gameplay[0], isGuessed=gameplay[1], guessed_num=gameplay[2], user_name=gameplay[3]) # call result function