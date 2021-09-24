print("Welcome to My Friends 1.0!")

# Advanced code Day One

# Question No 1
print("#####")
print("#" + '\t' + "#")
print("#" + '\t' + "#")
print("#" + '\t' + "#")
print("#####")

# Question No 2
print(" \n ")
print("#" + '\t' + "#")
print("#" + '\t' + "#")
print("#####")
print("#" + '\t' + "#")
print("#" + '\t' + "#")


# Practise programs (Create a heart)
print(" \n ")
print("* *   * *")
print("*" + '\t' + "*" + '\t' + "*")
print("*" + '\t' + '\t' + "*")
print( " " + "*" +"   " +"  " +"*")
print('\t' + "*")


# ######Day 2 Practise problem########



customer1="Charlie";
amount=60;
stuff="bread and milk"

print("My customer  named  %s bought a $ %d worth of  %s  " %( customer1, amount, stuff) )

# Day 2 Home work
friend_1_name = "Anita Reynolds"
friend_1_email = "anita.reynolds@example.com"
friend_1_age = 18
friend_1_the_best = True

friend_2_name = "Haleemath"
friend_2_email = "haleema@example.com"
friend_3_age = 30
friend_4_the_best = False


print("%s , %d years old Email: %s " % (friend_1_name, friend_1_age, friend_1_email))
# Advanced Homework

name="sameena"

day="Tuesday"

print("Good Day %s ! %s is a perfect day to learn Python " %(name, day));

# #####Day 3 Homework#######
#   Question1
friends = [
["Anita Reynolds", "anita.reynolds@example.com", 18, True],
["Carl Steward", "carl.steward@example.com", 21, False],
["Haleemath Sameena", "sameena@example.com", 34, True],

]

# Question 2
for friend in friends:
    print(friend[0] + '\t' + str(friend[2]) + '\t' + "years old" + '\t' + "Email:" + '\t' + friend[1])

# Question 3
friends = [
["Anita Reynolds", "anita.reynolds@example.com", 18, True],
["Carl Steward", "carl.steward@example.com", 21, False],
["Haleemath Sameena", "sameena@example.com", 34, True],

]
for friend in friends:
    if(friend[3]==True):
        print(friend[0]);

# Day 3 Homework Advanced level


phoneNumber = 'What is your phone number? '

value=input(phoneNumber);

length=len(str(value))
if(length == 10) and value.isdigit():
    print("valid number")

else:
    print("User input is not valid")


#######Day 4 Homework#######

print("Select the following option")
print('A: All friends')
print('B: Best friend')
Options='Type A or B here:'
Select_value =input(Options)

for i in friends:
    if Select_value == 'A':
        print(i[0])
    if Select_value == 'B':
        if i[3]==True:
            print(i[0])

#######Day 4 Homework Advanced
import random
a = random.randint(1,10)
user_input='Guess Any number between 1 and 10:'
guess=input(user_input);
if(a== int(guess)):
    print("your guess is right, The number is "+guess);
else:
    print("Your Guess was wrong")
    print("You Guessed ....." + guess)
    print("The original number is ...")
    print(a)

