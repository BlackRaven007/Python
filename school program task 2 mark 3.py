# I have imported os so that I will be able to make the file and open it
import os
# This is the number of class files i will be making
number_of_classes = 3
number_of_files = 4


def creating_classes(num_files):
    # This will generate the numbers 1 to 3 for the three different classes to be
    # used in the file name
    for x in range(1, num_files):
        # This will create the class1, class2, class3 .csv file if it does not exist.
        # If there is a file called the same as one of the files it does not create that one
        # It will just create the missing ones
        if not os.path.exists("class" + str(x) + ".csv"):
            file = open("class" + str(x) + ".csv", "w")
            file.close()

    
def get_player_class_and_score():
    # This sets the classes variable to 0
    school_classes = 0
    # This sets the score variable to -1

    # This sets the FirstClassChosen to equal to True
    first_class_chosen = True
    # This is a loop created so that the user can only enter a valid class number
    while school_classes < 1 or school_classes > 3:
        # This is an if statement which is only executed if FirstClassChosen equals to False
        if not first_class_chosen:
            # This is a message sent out to the user to remind them
            # that they can only insert a valid class number
            print("\nYou are only allowed to choose classes from 1 to " + str(number_of_classes))
        # This changes the variable from True to False so that it will go to the if statement above if the
        # user enters in a invalid number
        first_class_chosen = False
        # This will make the program tell the user to enter in a class number, it will also make the program try
        # asking the message until the uses enters a valid answer
        try:
            school_classes = int(input("Please enter the class you are in (1 to " + str(number_of_classes) + "):\t"))
        # This will turn the users answer to 0,which is also not valid, only if their answer contains letters
        except ValueError:
            school_classes = 0

    # This will ask for the users name
    name = input("Please enter the new player's name:\t")
    # This asks for the players score
    user_score = int(input("Please enter "+name+"'s score:\t"))
    # This is a loop created so that the user can only enter a score between 0 and 10
    while user_score < 0 or user_score > 10:
        try:
            user_score = int(input("You can only enter a score between 0 and 10. Please enter "+name+"'s score:\t"))

        # This will tell the user that their score in invalid and it turn the users answer to -1, which is also
        # not valid and makes the user try again.
        except ValueError:
            print("Invalid number")
            user_score = -1
    return name, school_classes, user_score


def save_score_to_file(name, school_classes, user_score):
    # This will set the variable namefound to False
    namefound = False
    # This will open the correct file, so that it can be written on, using the data gained from the
    # previous function
    scores_file = open("class" + str(school_classes) + ".csv", "r")
    scores_list = scores_file.readlines()
    scores_file.close()
    # This splits the names and scores already in there
    for x in range(0, len(scores_list)):
        list_name = scores_list[x].split(",")
        # This will then search for the name, given by the user, to the names in the file
        if name == list_name[0]:
            # If the name is found it will change the variable namefound to True
            namefound = True

    # If the variable namefound equals True, it will tell the user that the name is
    # already in use and they have to choose a different one
    if namefound:
            print("This name is already in use. Please choose a different name")
    else:
        # If the variable does not equal to True, then the program knows that it does not exist yet
        # This will again open the file and save the players name and score into the file
        result_file = open("class" + str(school_classes) + ".csv", "a")
        newline = (name + "," + str(user_score) + "\n")
        result_file.write(newline)
        result_file.close()
        # This will inform the user that the players name and score is added to the classes file
        print(name + "'s high score has been added to class " + str(school_classes) + " database!")

# Main program
creating_classes(number_of_files)
player, classes, score = get_player_class_and_score()
save_score_to_file(player, classes, score)
