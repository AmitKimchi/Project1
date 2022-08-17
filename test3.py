from random import randint
num = randint(1,9)
guessnum=int(input("Enter the selected number: "))
print(num)
while num!= guessnum:
    if guessnum < num:
        print("Higher")
        print(num)
    else:
        print("Lower")
        print(num)
    guessnum = int(input("Enter the selected number: "))
print("You did it you fucking ni**er")
print(num)
