# import the required modules
import os
import random
import csv     # imports the csv module
import time

# set constant max number of classes
MAX_NUMBER_OF_CLASSES = 3


# description: this function reads the pupils data from file
# parameters: the required class number
# return: a list containing the pupils data from file
def read_pupil_data(chosen_class):
    data_list = []  # initialise data_list
    if os.path.exists("class" + str(chosen_class) + ".csv"):    # checks if the class file exists
        file = open("class" + str(chosen_class) + ".csv", 'r')   # opens the csv file
        try:    # catches any exceptions when trying to read the file
            reader = csv.reader(file)  # creates the reader object and populates it with data
            data_list = list(reader)    # changes the data to a list under data_list
        finally:
            file.close()    # this will close the file even if there was an exception
    return data_list    # this will return the variable containing the pupils data


# description: this allows the user to see and choose from the menu
# parameters: none
# return: it returns an integer representing the users choice
def get_menu_selection():
    user_choice = 0     # initialise user_choice
    first = True    # initialise first
    while user_choice < 1 or user_choice > 5:   # whatever indented under it will run as long as user_choice is <1 or >5
        if not first:   # this checks if first equals False and if so, it will run whatever is indented under it
            print("Please try again using a whole number and a number from one of the options")     # outputs the text
        first = False   # reinitialise first
        print("\nPress \'1\' to play the game")
        print("Press \'2\' to view in alphabetical order with each student’s highest score for the tests")
        print("Press \'3\' to view scores by highest, highest to lowest")
        print("Press \'4\' to view scores by average, highest to lowest")
        print("Press \'5\' to exit")
        try:    # catches any exceptions when user enters their choice
            user_choice = int(input("\nPlease enter your choice from above:\t"))  # outputs text & takes input from user
        except ValueError:  # catches an error exception
            user_choice = 0     # reinitialise user_choice
    return user_choice  # this will return the variable containing the users choice


# description: this function receives which class the user is in
# parameters: none
# return: it returns an integer representing the users class
def get_class_num():
    class_num = 0   # initialise class_num
    while True:     # whatever indented under it will run as long as True equals True, which is always
        try:    # catches any exceptions when user enters their class
            class_num = int(input("\nPlease enter the class you are in (1 to " + str(MAX_NUMBER_OF_CLASSES) + "):\t"))
        except ValueError:  # catches an error exception
            class_num = 0     # reinitialise class_num

        if class_num < 1 or class_num > 3:  # indented under it will run if class_num is smaller than 1 or bigger than 3
            print("\nYou are only allowed to choose classes from 1 to " + str(MAX_NUMBER_OF_CLASSES))   # outputs text
        else:
            break   # this will exit the while loop if class_num not less than 1 or more than 3
    return class_num  # this will return the variable containing the class number
            

# description: this function allows the user to play the game
# parameters: none
# return: it returns an integer representing the users score and a string representing their name
def play_the_game():
    # Initialise local variables
    tries = 0
    score = 0
    low_number = 0
    high_number = 12
    
    username = input("Please enter your name here:\t")  # outputs text & takes input from user
    username = username.title()
    print("\nHello " + username + ", here are some questions for you to answer.")   # outputs text
    while tries != 10:   # whatever indented under it will run as long as tries do not equal to 10
        first_number = random.randint(low_number, high_number)   # initialise first_number
        operators = ['*', '-', '+']   # initialise operators
        operator = random.choice(operators)   # initialise operator
        last_number = random.randint(low_number, high_number)   # initialise last_number
        computer_answer = eval(str(first_number) + operator + str(last_number))   # initialise computer_answer
        while computer_answer < 0:   # whatever indented under it will run as long as computer_answer less than 0
            first_number = random.randint(low_number, high_number)   # reinitialise first_number
            computer_answer = eval(str(first_number) + operator + str(last_number))   # reinitialise computer_answer
        if operator == '*':   # this checks if operator equals * and if so, it will run whatever is indented under it
            operator = "x"  # this switches the star symbol to a x symbol to make it clearer for kids to multiply
        question = ("What does {} {} {} equal to?\t".format(first_number, operator, last_number))  # initialise question
        tries += 1  # updated variable to add 1
        valid = True   # initialise valid
        while True:     # whatever indented under it will run as long as True equals True, which is always
            if not valid:   # this checks if valid equals False and if so, it will run whatever is indented under it
                print("Please try again using a whole number.\n")   # outputs text
            try:    # catches any exceptions when user enters their choice
                print(question)   # outputs variable
                user_answer = int(input("Enter answer under here.\n"))  # outputs text & takes input from user
            except ValueError:  # catches an error exception
                valid = False   # reinitialise valid
            else:
                # This bit compares the user answer to the correct answer and tell the user if they are right or wrong.
                if user_answer == computer_answer:   # this checks if user_answer equals computer_answer
                    print("That is the correct answer\n\n")   # outputs text
                    score += 1  # updated variable to add 1
                else:
                    print("That is not the correct answer.\nThe correct answer was", computer_answer, "\n")  # show text
                break   # this will exit the while loop if user_answer not equal to computer_answer
    if score < 5:   # this checks if score less than 5
        print("Nice try. You got", score, "out of 10, Better luck next tries")   # outputs text
    elif score >= 10:   # this checks if score equals to or bigger than 10
        print("Congrats, you got", score, "out of 10, you win")   # outputs text
    else:
        print("Well done. You got", score, "out of 10, Next tries aim for 10 out of 10")   # outputs text
    return username, score  # it will return two variables, one containing their name and one containing the users score


# description: this function saves the score and name of the player in the classes file
# parameters: the pupils records, their name, their score and their class number
# return: none
def save_player_and_score(pupil_records, username, score, class_num):
    # filters the list to only contain the pupil we want to update and assign it to pupil_to_update
    pupil_to_update = [item for item in pupil_records if item[0] == username]
    if len(pupil_to_update) > 0:    # making sure that pupil exist in the list
        pupil_to_update[0][3] = pupil_to_update[0][2]   # getting rid of oldest score and adding a new score
        pupil_to_update[0][2] = pupil_to_update[0][1]   # moving the scores across
        pupil_to_update[0][1] = str(score)   # moving the scores across
    else:
        pupil_records.append([username, str(score), "", ""])    # this adds new user and score

    file = open("class" + str(class_num) + ".csv", 'w', newline='')   # opens the csv file
    try:    # catches any exceptions when user enters their choice
        a = csv.writer(file, delimiter=',')     # this creates a csv writer
        a.writerows(pupil_records)      # writes all the records from the list in csv format
        print(username + "'s high score has been added to the class " + str(class_num) + " database!")  # outputs text
    finally:
        file.close()    # this will close the file even if there was an exception



# main program
choice = 0  # initialise choice
while choice != 5:     # whatever indented under it will run as long as choice is not equal to 5
    pupil_class = get_class_num()   # pupil_class will hold whatever the function get_class_num returns
    pupil_data = read_pupil_data(pupil_class)  # this runs the function which read the pupils data & names it pupil_data
    time.sleep(2)   # this makes the program wait for 2 seconds before carrying on the program
    choice = get_menu_selection()  # this runs the function which prints out the menu & names it choice

    if choice == 1:
        # play the game
        pupil_name, pupil_score = play_the_game()  # this runs the function which plays the game & saves the variables
        save_player_and_score(pupil_data, pupil_name, pupil_score, pupil_class)     # saves score/name in classes file
    elif choice == 2:
        # view all scores alphabetically
        pupil_data.sort()   # this sorts the list into alphabetical order
        print("\n\nAlphabetical order with each student’s highest score for the tests from class", pupil_class)
        print("\n" + '%-30s' % "Players Name" + " Score")   # this outputs text
        print('-' * 36)     # this underlines the headings above
        for pupil in pupil_data:    # this creates a for loop
            max_score = max(pupil[1], pupil[2], pupil[3])   # this compares all three scores to find the biggest
            print('%-30s' % pupil[0] + " " + max_score)    # this outputs the variable containing the names & high score
    elif choice == 3:
        # get max score for each pupil and sort the list using it (descending)
        pupil_data.sort(key=lambda pupil_record: max(pupil_record[1], pupil_record[2], pupil_record[3]), reverse=True)
        print("\n\nscores by highest, highest to lowest in class", pupil_class)     # this outputs the text and variable
        print("\n" + '%-30s' % "Players Name" + " Score")   # outputs the text
        print('-' * 36)     # this underlines the headings above
        for pupil in pupil_data:    # this creates a for loop
            max_score = max(pupil[1], pupil[2], pupil[3])   # this compares all three scores to find the biggest
            print('%-30s' % pupil[0] + " " + max_score)    # this outputs the variable containing the names & high score
