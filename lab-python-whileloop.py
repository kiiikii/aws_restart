import random

print("welcome to guess number")
print("try guess my number")

number = random.randint(1,10)
isRight = False

while isRight != True:
    guess = input("Guess number 1-10: ")
    if int(guess) == number:
        print("{}, its correct! You win!".format(guess))
        isRight = True
    else:
        print("{}, sorry its incorrect. Try Again".format(guess))
    

