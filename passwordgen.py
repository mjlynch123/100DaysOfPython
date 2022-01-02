import random
from random import choice


special_characters = ['!', '@', '#', '$', '%', '&', '?']

num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
               'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Password can be only be a max of 25 characters")

letter_amount = int(input("How many letters would you like in your password?: "))
number_amount = int(input("How many numbers would you like in your password?: "))
character_amount = int(input("How many characters do you want in your password?: "))

all_add = letter_amount + number_amount + character_amount

if all_add <= 25:
    password = ''
    chose = []

    # These for loops get the number that is desired and then add the amount of items to the chose list
    # We add one to the letter, number, character amounts because we would get one less than desired if we didn't
    for char in range(1, letter_amount + 1):
        rand_char = choice(letter_list)
        chose.append(rand_char)

    for num in range(1, number_amount + 1):
        rand_number = choice(num_list)
        chose.append(rand_number)

    for character in range(1, character_amount + 1):
        rand_special = choice(special_characters)
        chose.append(rand_special)


    random.shuffle(chose)
    joined = "".join(chose)
    password = joined

    print(f"Your passowrd is: {password}")
else:
    print("Sorry password must be 25 characters or less")