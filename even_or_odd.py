number = int(input("Please enter a number: "))

if number % 4 == 0:
    print("Number is even and divisble by 4!")
elif number % 2 == 0:
    print("Number is even!")
else:
    print("Number is odd!")

#Adding all even numbers in the range of 1 to 20
total = 0
for numbers in range(1, 21, 2):
    total += numbers
print(total)