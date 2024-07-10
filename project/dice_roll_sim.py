import random

print('Welcome to dice simulator!!\n')

def roll_dice(dices) -> list[int]:
  count = []

  if 0 < dices <= 6 :
    for i in range(1,dices + 1) :
      count.append(random.randint(1,6))
  else :
    print('Please enter a number between 1 and 6')

  return count

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

def dice_draw(dice_values) :
  for line in range(5) :
    for die in dice_values :
      print(DICE_ART.get(die)[line],end = '')
    print()


user_input = int(input('How many dices you want to roll? (1-6) : '))
roll_result = roll_dice(user_input,)
print(roll_result,'\n')

dice = dice_draw(roll_result)