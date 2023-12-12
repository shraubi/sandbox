import random

def game():
    number = random.randint(0, 10)
    attempts = 0
    
    while True:
        try:
            guess = int(input("ебашь "))
            attempts += 1
            if guess == number:
                break
            elif guess < number:
                print("хуй тоби, больше")
            else:
                print("опять хуй, меньше")
        except ValueError:
            print("хуйня якась, введи число")

    print(f"тебе понадобилось {attempts} попытки")

game()
