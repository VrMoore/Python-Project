import random
print('Welcome to Rock, Paper and Scissor game!\nYou have to take a guess\n')

def play_game(player_choice) :
  if player_choice == 'y' :
    computer_guess = random.choice(['rock', 'paper', 'scissor'])
    player_score = computer_score = 0
    player_guess = input('Input : ')

    player_rock = (player_guess == 'rock' and computer_guess == 'scissor')
    player_paper = (player_guess == 'paper' and computer_guess == 'rock')
    player_scissor = (player_guess == 'scissor' and computer_guess == 'paper')

    if player_rock or player_paper or player_scissor :
      print('\nYou Win!')

      print(f"""
      Your guess : {player_guess}
      computer guess : {computer_guess}
      """)


      player_score += 1 

    elif player_choice == computer_guess :
      print('\nIt\'s a tie!')

      print(f"""
      Your guess : {player_guess}
      computer guess : {computer_guess}
      """)

    elif player_guess != computer_guess :
      print('\nYou Lose!')
      print(f"""
      Your guess : {player_guess}
      computer guess : {computer_guess}
      """)

      computer_score += 1

    condition = input('Play game again? (y/n) : ')
    if condition == 'y' :
      play_game(player_choice)
    elif condition == 'n' :
      print(f"""
      Your score : {player_score}
      Computer score : {computer_score}
      """)
      print('\nThank you for playing the game :)')
      quit()
    else : 
      print('Invalid Input, Try again')
      play_game(player_choice)

  elif player_choice == 'n' :
    print('Thank you for playing the game :)')
    quit()
  else :
    print('Invalid Input, Try again')

state = input('Do you wanna to play? (y/n) : ')
play_game(state)