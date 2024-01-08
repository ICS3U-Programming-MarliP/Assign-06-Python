#!usr/bin/env python3
# Created By: Marli Peters
# Date: Jan. 7, 2023
# This program asks the user for a list
# then frames the list and displays it
# back to the user.

# function to frame list
def frame_list(user_list):
    # setting counter to length of list
    counter = len(user_list)

    # find length of longest string in list
    res = max(len(ele) for ele in user_list)

    # set top and bottom border to the right size
    border = "*" * (res + 5)

    # print the top border
    print(border)

    # print each word on list with borders the right size
    for counter in range(counter):
        spaces = res - len(user_list[counter])
        print("*", user_list[counter], spaces * " ", "*")

    # print bottom border
    print(border)

    return

    # main function to run the code
def main():
    # welcome message
    print(
        "Hello and welcome to the framed list program! You will be asked to enter a list of words then it will be put in a frame of asterisks. Enter blank to stop adding words.\n"
    )

    # create user list and word variable to add to list
    user_list = []
    user_word = "Placeholder"

    # continue asking user for words to add to list until they enter blank
    while user_word != "":
        user_word = str(input("Enter a word: "))
        if user_word != "":
            user_list.append(user_word)
    print("")

    # run the border function
    frame_list(user_list)


if __name__ == "__main__":
    main()
