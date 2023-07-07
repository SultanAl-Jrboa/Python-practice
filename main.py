# print تعني طباعة , input تعني ادخال
#print("Hello " + input("What is your name"))

# تم تعريف str لحمل قيمة من المستخدم
#str = input("What is your name? ")
# len لحساب طول القيمة
#print(len(str))

#name = input("What is your name?")
#print(name)

#num1 = input("a: ")
#num2 = input("b: ")

#print("b:" + num2)
#print("a:" + num1)

#print("Welcome to the Band Name Generator.")

#print("What's name of the city you grew up in?")
#city = input()
#print("What's your pet's name?")
#pet = input()
#print("Your band name could be " + city + "" + pet)

#
# two_numbers = input("Type a two digit number: ")
# print(int(two_numbers[0]) + int(two_numbers[1]))
# first_num = two_numbers[0]
# seconde_num = two_numbers[1]
#
# the_final_result = int(first_num) + int(seconde_num)
# print(the_final_result)
#
# print(3 * (3 + 3) / 3 - 3)

# height = input("enter your height:  ")
# weight = input("enter your weight:  ")
#
# height1 = (float(height))
# weight2 = (int(weight))
#
# result = int(weight2 / (height1 * height1))
# print(result)


#height = input("enter your height : ")
#weight = input("enter your weight : ")
#w = float(weight)
#h = float(height)
#BMI = (w/(h ** 2))
#BMI_int = int(BMI)
#print(BMI_int)


#
# age = int(input("What is your current age? "))
# ags_as_int = int(age)
# years_remaning = 90 - ags_as_int
#
# the_days = (years_remaning * 365)
# the_weeks = (years_remaning * 52)
# the_months = (years_remaning * 12)
#
# print(f"You have {the_days} days, {the_weeks} weeks, and {the_months} months left.")


# print("Welcome to the tip calculater.")
# bill = float(input("What was the total bull? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12 , or 15? "))
# people = int(input("How many people to split the bill? "))
#
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



# number = int(input("Which number do you want to check? "))
#
# if number % 2:
#     print("This is an odd number.")
#
# else:
#     print("This is even number")
#



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

print("Welcoem to the Love calculater!")
name1 = input(("What is your name? \n"))
name2 = input(("What is her name? \n"))

combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score},you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score},you are alright together.")
else:
    print(f"Your score is {love_score}")

