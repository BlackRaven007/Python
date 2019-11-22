# I have imported os so that i will be able to make the file and open it
import os


def creating_class_one():
    # This will create the class1 file if it does not exist.
    # If there is a file called class1 it does not create one
    if not os.path.exists("class1"):
        file = open("class1", "w")
        file.close()


def add_player_and_score():
    # This line of code asks if the payer is in class 1, 2 or 3.
    classes = int(input("Please enter in the class you are in (1, 2 or 3):\t"))
    # This asks what's the players name is.
    name = input("Please enter the new player's name:\t")
    # This asks what's the players score is.
    score = int(input("Please enter "+name+"'s score:\t"))
    # The following few lines is the program which chose which database to save to (1, 2 or 3).
    if classes == '1':
        # This opens the class1 file so that it can write on it.
        scores_file = open("class1.csv", "r")
        scores_list = scores_file.readlines()
        scores_file.close()
        result_file = open("class1.csv", "a")
        # This searches the database for the players name.
        for x in range(0, len(scores_list)):
            list_name = scores_list[x].split(",")[0].strip()
        # If the players name is found it will tell the user that the name is already exists.
            if name == list_name:
                print("This name is already in use. Please choose a different name")
        else:
            # If the name does not exist it will write the players name an score to the database.
            newline = (name + "," + str(score) + "\n")
            result_file.write(newline)
        # This closes the database and tells the user it has been added to the database
        # successfully.
        result_file.close()
        print(name+"'s high score has been added to class 1 database!")

    elif classes == '2':
                # This opens the class2 file so that it can write on it.
                scores_file = open("class2.csv", "r")
                scores_list = scores_file.readlines()
                scores_file.close()
                result_file = open("class2.csv", "a")
                # This searches the database for the players name.
                for x in range(0, len(scores_list)):
                    list_name = scores_list[x].split()
                    # If the players name is found it will tell the user that the name is already exists.
                    if name == list_name:
                        print("This name is already in use. Please choose a different name")
                else:
                    # If the name does not exist it will write the players name an score to the
                    # database.
                    newline = (name + "," + str(score) + "\n") 
                    result_file.write(newline)
                # This closes the database and tells the user it has been added to the database
                # successfully.
                result_file.close()
                print("Player and high score has been added to class 2 database!")
    elif classes == '3':
                # This opens the class2 file so that it can write on it.
                scores_file = open("class3.csv", "r")
                scores_list = scores_file.readlines()
                scores_file.close()
                result_file = open("class3.csv", "a")
                # This searches the database for the players name.
                for x in range(0, len(scores_list)):
                    list_name = scores_list[x].split()
                    # If the players name is found it will tell the user that the name is already exists.
                    if name == list_name:
                        print("This name is already in use. Please choose a different name")
                else:
                    # If the name does not exist it will write the players name an score to the
                    # database.
                    newline = (name + "," + str(score) + "\n")
                    result_file.write(newline)
                # This closes the database and tells the user it has been added to the database
                # successfully.
                result_file.close()
                print("Player and high score has been added to class 3 database!")

# Main program
creating_class_one()
add_player_and_score()
