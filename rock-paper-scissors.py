import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_for_computer = [rock, paper, scissors]
#Write your code below this line 👇
print("What would you like to throw: Type 0 for rock, 1 for paper and 2 for scissors")

player_score = 0
comp_score = 0

chose = input()

if chose == '0':
  chose = rock
elif chose == '1':
  chose = paper
elif chose == '2':
  chose = scissors
else:
  print("Sorry I didn't quite understand that.")

computer_choice = random.choice(choices_for_computer)

choices = []

choices.append(chose)
choices.append(computer_choice)

print("Player Choice: \n" + choices[0])
print("Computer Choice: \n" + choices[1])

if choices[0] == rock and choices[1] == paper:
  print("Player scored a point")
  player_score += 1
  print(player_score)
  print(comp_score)
elif choices [0] == paper and choices[1] == rock:
  print("Computer scores a point") 
  comp_score += 1
  print(player_score)
  print(comp_score)
elif choices[0] == rock and choices[1] == scissors:
  print("Player scored")
  player_score += 1
  print(player_score)
  print(comp_score)
elif choices[0] == scissors and choices[1] == rock:
  print("Computer scores a point") 
  comp_score += 1
  print(player_score)
  print(comp_score)
elif choices[0] == scissors and choices[1] == paper:
  print("Player scored a point")
  player_score += 1
  print(player_score)
  print(comp_score)
elif choices[0] == paper and choices[1] == scissors:
  print("Computer scores a point") 
  comp_score += 1
  print(player_score)
  print(comp_score)
elif choices[0] == choices[1]:
  print("Tied. No point")