from random import randint

def random_number():
    return randint(1, 20)


def game_process(guess_count, guess, number, name):
    while(guess_count < 3):
        if(guess > 0 and number < 21):
            if(number > guess):
                print("\nYour guess is too low.")
            elif(number < guess):
                print("\nYour guess is too high.")
            else:
                return True, guess_count
        guess = int(input("Take a guess.\n"))
        guess_count += 1
    return False, guess_count