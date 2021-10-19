import random

Choice_one = input("choice 1: ")
Choice_two = input("choice 2: ")
Choice_three = input("choice 3: ")

choices = [Choice_one,Choice_two,Choice_three]
max = len(choices) - 1
i = random.randint(0,max)
chosen = choices[i]
print(chosen + " has been chosen!")
