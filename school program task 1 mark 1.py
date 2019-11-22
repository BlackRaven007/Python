# This inserts the random module which allows the computer to
# randomly chose something from a list.
import random
# This variable is to keep track of the number of correct answers the
# user has entered.
score = 0
    
# This is the program to create the question and generate the correct
# answer for that question.
# This chooses the first random number between 1 and 12 for the question.
first_number = random.randint(1, 12)
# This is the variable the operation is been held in.
operator = '+'
# This chooses the second random number between 1 and 12 for the question.
last_number = random.randint(1, 12)
# This is the variable the question is being held in.
question = ("What does {} {} {} equal to?\t".format(first_number, operator, last_number))
# This line is how the computer knows the correct answer for the
# question being asked.
computer_answer = eval(str(first_number) + operator + str(last_number))

# These two lines asks the user the question.
print(question)
user_answer = int(input("Enter answer under here.\n"))
# This bit compares the user answer to the correct answer and tell the user
# if they are right or wrong.
if user_answer == computer_answer:
    print("That is the correct answer\n\n")
    score += 1
else:
    print("That is not the correct answer.\nThe correct answer was", computer_answer, "\n")

# The problem with this code is that it only asks one question and is only
# able to to addition.
