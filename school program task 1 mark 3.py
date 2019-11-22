# This inserts the random module which allows the computer to randomly
# chose something from a list.
import random
# These are two variables to keep track of the number of correct answers the
# user has entered, the number of times questions were asked and the calculated answer
num_answered = 0
score = 0
low_number = 0
high_number = 12
computer_answer = 0
# This asks the user to input their name to be stored with their score in coming versions.
# It also welcomes them to the game.
valid = True
username = input("Please enter your name below here:\n")
while 0 == len(username) or len(username) > 50:
    if not valid:
        print("You must enter a username between 1 and 50 characters")
        username = input("Please enter your name below here:\n")
    valid = False
print("Hello " + username + ", here are some questions for you to answer.")
# This is the program to create the question and generate the correct
# answer for that question.
# This hopefully allows the questions to be asked only ten times.
while num_answered != 10:
    # This chooses the first random number between 0 and 12 for the question.
    first_number = random.randint(low_number, high_number)
    # This is the variable where all the  operations which is going to be used in the questions is been held in.
    operators = ['*', '-', '+']
    # This bit chooses one of the things randomly from '*', '-' and '+' in the middle bit variable.
    operator = random.choice(operators)
    # This chooses the second random number between 0 and 12 for the question.
    last_number = random.randint(low_number, high_number)
    # This line is how the computer knows the correct answer for the question being asked.
    computer_answer = eval(str(first_number) + operator + str(last_number))
    # Ensure correct answer is non negative.
    while computer_answer < 0: 
        first_number = random.randint(low_number, high_number)
        computer_answer = eval(str(first_number) + operator + str(last_number))
    question = ("What does {} {} {} equal to?\t".format(first_number, operator, last_number))
    
    num_answered += 1
    valid = True
    while True:
        if not valid:
            print("Please try again using a whole number.\n")
        valid = False
        try:
            print(question)
            user_answer = int(input("Enter answer under here.\n"))
        except ValueError:
            user_answer = 0
        else:
            # This bit compares the user answer to the correct answer and tell the user if they are right or wrong.
            if user_answer == computer_answer:
                print("That is the correct answer\n\n")
                score += 1
            else:
                print("That is not the correct answer.\nThe correct answer was", computer_answer, "\n")
            break
# This tells the user how many out of ten they got correct.
if score < 5:
    print("Nice try. You got", score, "out of 10, Better luck next time")
elif score >= 10:
    print("Congrats, you got", score, "out of 10, you win")
else:
    print("Well done. You got", score, "out of 10, Next time aim for 10 out of 10")
