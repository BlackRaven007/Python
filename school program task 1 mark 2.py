# This inserts the random module which allows the computer to randomly
# chose something from a list.
import random
# These are two variables to keep track of the number of correct answers the
# user has entered, the number of times questions were asked and the calculated answer
time = 0
score = 0

# This asks the user to input their name to be stored with their score in coming versions.
# It also welcomes them to the game.
username = input("Please enter your name below here.\n")
print("Hello", username, ". Here are some questions for you to answer.")
# This is the program to create the question and generate the correct
# answer for that question.
# This hopefully allows the questions to be asked only ten times.
while time != 10:
    # This chooses the first random number between 1 and 12 for the question.
    first_number = random.randint(1, 12)
    # This is the variable where all the  operations which is going to be used in the questions is been held in.
    operators = ['*', '-', '+']
    # This bit chooses one of the things randomly from '*', '-' and '+' in the middle bit variable.
    operator = random.choice(operators)
    # This chooses the second random number between 1 and 12 for the question.
    last_number = random.randint(1, 12)
    # This is the variable the question is being held in.
    question = ("What does {} {} {} equal to?\t".format(first_number, operator, last_number))
    # This line is how the computer knows the correct answer for the question being asked.
    computer_answer = eval(str(first_number) + operator + str(last_number))
    # This lines asks the user the question.
    print(question)
    user_answer = int(input("Enter answer under here.\n"))
    # This bit compares the user answer to the correct answer and tell the user if they are right or wrong.
    if user_answer == computer_answer:
        print("That is the correct answer\n\n")
        score += 1
    else:
        print("That is not the correct answer.\nThe correct answer was", computer_answer, "\n")

# This tells the user how many out of ten they got correct.
if score < 5:
    print("Nice try. You got", score, "out of 10, Better luck next time")
elif score >= 10:
    print("Congrats, you got", score, "out of 10, you win")
else:
    print("Well done. You got", score, "out of 10, Next time aim for 10 out of 10")
# The problem with this version is that the questions are been run in a continuous loop
