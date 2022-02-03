import random


def guess_random():
    randomnumber = random.choice(range(1, 101))
    return randomnumber


randomguess = guess_random()
print(randomguess)

easy = 1
hard = 10


while easy <= 5:
    for guess in range(5):
        user_guess = int(input("guess the num: "))
        print(user_guess)
        if user_guess != randomguess:
            pass
        else:
            print("you are right")

            break


        easy += 1
