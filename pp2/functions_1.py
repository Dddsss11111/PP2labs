# 1 A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

# def toGrams(a):
#     return(a * 28,3495231)


# 2 Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

# def celcius(F):
#     return (F - 32) * 5 / 9


# 3 Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

# def solve(numheads, numlegs):
#     # 2x + y = numlegs / 2
#     # x + y = numheads
#     x = numlegs / 2 - numheads
#     y = numheads - x
#     return x, y

# print(solve(35, 94))


# 4 You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list

# def filter_prime(numbers):
#     filtered_list = []
#     for i in numbers:
#         f = True
#         for j in range(2, int(i)):
#             if int(i) % j == 0:
#                 f = False
#                 break
#         if(f):
#             filtered_list.append(int(i))
#     return filtered_list

# # numbers = [i for i in range(1, 100)]
# numbers = input().split(" ")
# print(filter_prime(numbers))


# 5 Write a function that accepts string from user and print all permutations of that string.

# from itertools import permutations

# def print_permutations(input_string):
#     perms = permutations(input_string)
#     for perm in perms:
#         print(''.join(perm))

# user_input = input("Enter a string: ")
# print_permutations(user_input)


# 6 Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

# def reverse(string):
#     string = string.split(" ")
#     res = ""
#     for i in reversed(string):
#         res += i + " "
#     return res
# print(reverse(input()))


# 7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def has_33(nums) -> bool:
#     for i in range(0, len(nums) - 1):
#         if(nums[i] == 3):
#             if(nums[i + 1] == 3):
#                 return True
#             i += 2
#     return False

# has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3])


# 8 Write a function that takes in a list of integers and returns True if it contains 007 in order

# def spy_game(nums):
#     spy = [0, 0, 7]
#     for i in nums:
#         if len(spy) == 0:
#             return True
#         if i == spy[0]:
#             spy.pop(0)
#     if len(spy) == 0:
#         return True
#     return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))


# 9 Write a function that computes the volume of a sphere given its radius.

# def sphere_volume(R):
#     return R ** 3 * 4 / 3


# 10 Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

# def unique(numbers):
#     unique_list = []
#     for i in numbers:
#         if i not in unique_list:
#             unique_list.append(i)
#     return unique_list


# 11 Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

# def is_palindrome(word):
#     word = "".join(word.lower().split())
#     if word == word[::-1]:
#         return "it's palindrome"
#     return "not palindrome"

# print(is_palindrome("Kazak"))


# 12 Define a function histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

# def histogram(li):
#     for i in li:
#         print("*" * i)
# histogram([4, 9, 7])


# 13 Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:

# from random import randint

# def game():
#     name = input("Hello! What is your name?\n")
#     print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
#     guess_count = 0
#     number = randint(1, 20)
#     guess = 0
#     while(guess_count < 3):
#         if(guess > 0 and number < 21):
#             if(number > guess):
#                 print("\nYour guess is too low.")
#             elif(number < guess):
#                 print("\nYour guess is too high.")
#             else:
#                 print(f"\nGood job, {name}! You guessed my number in {guess_count} guesses!")
#                 return 0
#         guess = int(input("Take a guess.\n"))
#         guess_count += 1
#     print(f"\nGood game {name}. Number was {number} Good luck next time!")

# game()


# 14 Same game, but import functions from another python file

# from Game import random_number, game_process

# def game():
#     name = input("Hello! What is your name?\n")
#     print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
#     number = random_number()
#     win, guess_count = game_process(0, 0, number, name)
#     print(f"\nGood job, {name}! You guessed my number in {guess_count} guesses!") if(win) else print(f"\nGood game {name}. Number was {number} Good luck next time!")

# game()