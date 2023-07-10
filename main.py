
       #{Band Name Generator}#

#print("Welcome to the Band Name Generator.")
#print("What's name of the city you grew up in?")
#city = input()
#print("What's your pet's name?")
#pet = input()
#print("Your band name could be " + city + "" + pet)

              #{The Number Game}#

# two_numbers = input("Type a two digit number: ")
# print(int(two_numbers[0]) + int(two_numbers[1]))
# first_num = two_numbers[0]
# seconde_num = two_numbers[1]
# the_final_result = int(first_num) + int(seconde_num)
# print(the_final_result)

           #{BMI}#

#height = input("enter your height : ")
#weight = input("enter your weight : ")
#w = float(weight)
#h = float(height)
#BMI = (w/(h ** 2))
#BMI_int = int(BMI)
#print(BMI_int)

           #{Calculate The Months and weeks and days an your age}#

# age = int(input("What is your current age? "))
# ags_as_int = int(age)
# years_remaning = 90 - ags_as_int
# the_days = (years_remaning * 365)
# the_weeks = (years_remaning * 52)
# the_months = (years_remaning * 12)
# print(f"You have {the_days} days, {the_weeks} weeks, and {the_months} months left.")

         #{Tip Calculater}#

# print("Welcome to the tip calculater.")
# bill = float(input("What was the total bull? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12 , or 15? "))
# people = int(input("How many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
#
# print(f"Each person should pay: ${final_amount} ")

             #{Rollercoaster Game}#

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercostaer!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         bill = 5
#         print("Child tickets pay $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets pay $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going be ok. Have a free ride on us!")
#     else:
#         bill = 12
#     print("Adult tickets pay $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#        bill += 3
#        print(f"Your final bill is ${bill}")
#
#     else:
#      print("Sorry, you have grow taller before you can ride.")

               #{Tip Calculater}#

# number = int(input("Which number do you want to check? "))
#
# if number % 2:
#     print("This is an odd number.")
#
# else:
#     print("This is even number")

             #{Body Mass Index (BMI)}#

# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
# mult_the_height = (height * height)
# bim = (weight / mult_the_height)
# final_bim = round(bim)
#
# if final_bim <= 18.5:
#     print(f"Your BMI is {final_bim}, you are underweight.")
# elif final_bim <= 25:
#     print(f"Your BMI is {final_bim}, you have a normal weight.")
# elif final_bim <= 30:
#     print(f"Your BMI is {final_bim},you are slightly overweight.")
# elif final_bim <= 35:
#     print(f"Your BMI is {final_bim},you are obese.")
# elif final_bim > 35:
#     print(f"Your BMI is {final_bim},you are clinically obese")

          #{Culcaletor For Leap Yers}#

# the_year = int(input("Which year do you want to check? "))
#
# if the_year % 4 == 0:
#     print("Leap year.")
# elif the_year % 100 == 0:
#     print("Not leap year.")
# elif the_year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

              #{Python Pizza Deliveries!}

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")

                #{Love Calcilater}#

# print("Welcoem to the Love calculater!")
# name1 = input(("What is your name? \n"))
# name2 = input(("What is her name? \n"))

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true = t + r + u + e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))
# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score},you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your score is {love_score},you are alright together.")
# else:
#     print(f"Your score is {love_score}")

                    #{Treasure Island Game!}#

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
# choice1 = input(("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")).lower()
#
# if choice1 == "left":
#    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
#    if choice2 == "wait":
#       choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
#    if choice3 == "red":
#        print("It's a room full of fire. Game Over.")
#    elif choice3 == "yellow":
#        print("You found the treasure! You Win!")
#    elif choice3 == "blue":
#        print("you enter a room of beasts. Game Over.")
#    else:
#        print("You chose a door that doesn't exist. Game Over.")
#    else:
#    print("You got attacked by angry trout. Game Over.")
#   else:
#    print("Fall into a hole. \n Game Over.")

         #{Random Number 1, 10}#

# import random
#
# random_int = random.randint(1, 10)
# print(random_int)
#
# random_float = random.random()
# print(random_float)

          #{if the number = 1 the output = Tails etc..}#

# import random
#
# Heads_or_Tails = random.randint(0, 1)
#
# if Heads_or_Tails == 1:
#     print("Heads")
# else:
#     print("Tails")

              #{Who will pay the?}#

# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
#
# person_who_will_pay = names[random_choice]
#
# print(person_who_will_pay + " is going to buy the meal today!")


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[0][1])

             #{Welcomt to the treeasure Map Game}#

# map1 = ['⬜️', '⬜️', '⬜️']
# map2 = ['⬜️', '⬜️', '⬜️']
# map3 = ['⬜️', '⬜️', '⬜️']
# map = [map1, map2, map3]
# print(f"{map1}\n{map2}\n{map3}")
#
# position = input(("Where do you want to put the treeasure? "))
#
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizontal - 1] = "X"
#
# print(f"{map1}\n{map2}\n{map3}")

           #{ Rock Paper Scissors Game}#

# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]
# user_choice = int(input(("What to you choice? Type 0 fot Rock, 1 for Paper or 2 for Scissors\n")))
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
#
# else:
#  print(game_images[user_choice])
#
# computer_choice = random.randint(0, 2)
# print("Computer choice")
# print(game_images[computer_choice])
#
# if user_choice == 0 and computer_choice ==2:
#     print("You win!")
# elif computer_choice ==0 and user_choice ==2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw")

             #{Calculates the average student height}#

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# the_av = len(student_heights)
# the_total = sum(student_heights)
# div = (the_total / the_av)
# print(round(div))

                 #{Calculates the highest score}#

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# the_total = max(student_scores)
# print(f"The highest score in the class is: {the_total}")

                 #{FizzBuzz Game!}#

# for number in range(1, 101):
#     if  number % 3 ==0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 ==0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)




                    #{PyPassword Generator}#

# import random                                     #an in-built module of Python that is used to generate random numbers in Python
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
#                         #Eazy Pass
#
# # password =""
# #
# # for char in range(1, nr_letters + 1):
# #     password += random.choice(letters)
# #
# # for char in range(1, nr_symbols + 1):
# #     password += random.choice(symbols)
# #
# # for char in range(1, nr_numbers + 1):
# #     password += random.choice(numbers)
# #
# # print(password)
#
#                      #Hard Pass
#
# password_list =[]                                  #all value in the list
#
# for char in range(1, nr_letters + 1):              #the range of the input user betwen (1 + input user + 1)
#     password_list.append(random.choice(letters))   #a pre-defined method used to add a single item to certain collection types
#
# for char in range(1, nr_symbols + 1):              #etc ^
#     password_list.append(random.choice(symbols))   #etc..
#
# for char in range(1, nr_numbers + 1):              #etc ^
#     password_list.append(random.choice(numbers))   #etc..
#
# random.shuffle(password_list)                      #for mex the number and symbols and letters
#
# password =""                                       #for git a password in the same line
# for char in password_list:
#     password += char                               #put the (char in the password)
#
# print(f"Your password is: {password}")             #print the password with (f) for add the mex variuble

          #{How to create Function}#

def my_function():    #first (def) and name of function():
print("Hello")
#print("Bye")

my_function()