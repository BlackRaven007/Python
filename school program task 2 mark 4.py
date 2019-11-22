
# I have imported os so that I will be able to make the file and open it
import os
# This is the number of class files i will be making
Number_of_classes = 3
# This creates a variable called PlayersNames
PlayersNames = []


def read_players_names(classes_num):
    # This will open the csv class file
    scores_file = open("class" + str(classes_num) + ".csv", "r")
    # Read all the lines into a list
    scores_list = scores_file.readlines()
    scores_file.close()

    # Loop through all the lines in the list
    for x in range(0, len(scores_list)):
        # Split each record into another array called line.
        # This line is split when it finds a comma
        line = scores_list[x].split(",")
        # The user name is the first item in the line array
        player_user = (classes_num, line[0])
        # Add the user name onto the PlayerNames array
        PlayersNames.append(player_user)


def creating_classes(classes_num):
    # This will create the class1, class2, class3 .csv file if it does not exist.
    # If there is a file called the same as one of the files it does not create that one
    # It will just create the missing ones
    for x in range(0, classes_num):
        # This will create the class1, class2, class3 .csv file if it does not exist.
        # If there is a file called the same as one of the files it does not create that one
        # It will just create the missing ones
        if not os.path.exists("class" + str(x+1) + ".csv"):
            file = open("class" + str(x+1) + ".csv", "w")
            file.close()
        # Read in all the names in this file
        read_players_names(x+1)


def is_name_already_in_use(name, classes_num):
    # This will set the variable namefound to False
    namefound = False

    # This searches for all the names, that already exists in the file, to the
    # name that the user has given
    for x in range(0, len(PlayersNames)):
        player_user = PlayersNames[x]
        # If the name is found it will change namefound to True
        if classes_num == player_user[0] and name == player_user[1]:
            namefound = True
    return namefound


def get_player_class_and_score():
    # This sets the classes variable to 0
    classes_num = 0
    user_score = -1
    name = ""
    # This sets the FirstClassChosen to equal to True
    while True:
        classes_num = 0
        user_score = -1
        first_class_chosen = True
        # This is a loop created so that the user can only enter a valid class number
        while classes_num < 1 or classes_num > 3:
            # This is an if statement which is only executed if FirstClassChosen equals to False
            if not first_class_chosen:
                # This is a message sent out to the user to remind them
                # that they can only insert a valid class number
                print("\nYou are only allowed to choose classes from 1 to " + str(Number_of_classes))
            # This changes the variable from True to False so that it will go to the if statement above if the
            # user enters in a invalid number
            first_class_chosen = False
        # This will make the program tell the user to enter in a class number, it will also make the program try
        # asking the message until the uses enters a valid answer
            try:
                classes_num = int(input("Please enter the class you are in (1 to " + str(Number_of_classes) + "):\t"))
        # This will turn the users answer to 0,which is also not valid, only if their answer contains letters
            except ValueError:
                classes_num = 0

    # This will ask for the users name and score
        valid = True
        name = input("Please enter the new player's name:\t")
        while 0 == len(name) or len(name) > 50:
            if not valid:
                print("You must enter a username between 1 and 50 characters")
                name = input("Please enter the new player's name:\t")
            valid = False
    # This is a loop created so that the user can only enter a score between 0 and 10
        try:
            user_score = int(input("Please enter "+name+"'s score:\t"))
        except ValueError:
                print("Invalid number. You must enter your score as an integer and between 0 and 10.")
                user_score = -1
        while user_score < 0 or user_score > 10:
            try:
                print("Score can only be between 0 and 10")
                user_score = int(input("Please enter "+name+"'s score:\t"))
        # This will tell the user that their score in invalid and it turn the users answer to -1, which is also
        # not valid and makes the user try again.
            except ValueError:
                print("Invalid number. You must enter your score as an integer and between 0 and 10.")
                user_score = -1
        if not is_name_already_in_use(name, classes_num):
            break
        else:
            print("This name is already in use for this class, please select a different name or class.")

    return name, classes_num, user_score


def save_score_to_file(name, classes_num, user_score):

    # If the variable does not equal to True, then the program knows that it does not exist yet
    # This will again open the file and save the players name and score into the file
    result_file = open("class" + str(classes_num) + ".csv", "a")
    newline = (name + "," + str(user_score) + "\n")
    result_file.write(newline)
    result_file.close()
    # This will inform the user that the players name and score is added to the classes file
    print(name + "'s high score has been added to class " + str(classes_num) + " database!")

# Main program
creating_classes(Number_of_classes)
player, classes, score = get_player_class_and_score()
save_score_to_file(player, classes, score)
