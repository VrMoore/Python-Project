import random
print('Welcome to Guessing Number Game\nYou have to guess the number between 1 and 15\n')

def play_game(condition) :
  user_score = 0
  comp_score = 0

  if condition == 'y' :
    print('\n','='*10,'The game start!','='*10,'\n')

    number = random.randint(1,15)
    user_input = int(input('enter your number guess : '))
    comp_input = number

    if user_input == comp_input : 
      print("You win")
      print(f"""
      Your guess : {user_input}
      computer guess : {comp_input}
      """)
      user_score += 1

    else :
      print("You Lose")
      print(f"""
      Your guess : {user_input}
      computer guess : {comp_input}
      """)
      comp_score += 1

    condition = input("Do you want to play the game again? (y/n)") 
    if condition == 'y' :
      play_game(condition)
    else :
      print(f"""
      Your score : {user_score}
      computer score : {comp_score}
      """)
      print('Thank you for playing the game :)')
      quit()

  elif condition == 'n' :
    print('Thank you for playing the game :)')
    quit()

  else :
    print('Invalid Input, Try again')


state = input("Do you want to play the game? (y/n) : ")
game = play_game(state)