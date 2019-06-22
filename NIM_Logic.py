
from time import sleep
import random
print("Welcome to NIM!")
delay = 1.0
sleep(delay)
total = float(input("How many balls to you want to play with?"))
def test_total():
    """
    Checks if it pass the criteria that the initial number af balls should be greater or equal to 15
    :return:
    """
    global total
    while total < 15:
        total = float(input("How many balls to you want to play with?"))
        # Keeps the number of balls to be greater than 15
def test_pick():
    """
    Checks the number of the balls a user picks. It must be less than 4 for all total greater than 4.
    :return:
    """
    global user_pick
    while user_pick > pickno or user_pick <= 0 or type(user_pick):
        user_pick = int(input("How many balls do you want to get? (Up to 4)"))
        #Keeps the number of balls picked by user to be between 0 and 4
def remain():
    """
    Calculates the remaining balls after each user pick.
    :return:
    """
    global total
    global user_pick
    total = int(total - user_pick)
    print("Remaining " + str(total))
def cmp_logic():
    """
    Finds the logic for the pick of the computer. If the number af balls remaining is a multiple of 5,
    the computer gets a random amount of balls. Otherwise, if the number is not divisible by 5, the computer gets the remainder
    of the division of the amount of balls remaining divided by 5.
    :return:
    """
    global total
    global comp_pick
    comp_pick = int(total % 5)
    #Computer picks randomly
    if comp_pick > pickno or comp_pick <= 0:
        comp_pick = random.randint(1, 4)
    sleep(delay)
    #Computer wins!!
    if comp_pick == total:
        print("Computer picks " + str(total) + "!")
        sleep(delay)
        print("Computer WINS!")
        total = 0
        exit()
    #Just a normal pick from the computer
    else:
        print("Computer picks " + str(comp_pick) + "!")
        sleep(delay)
        total = int(total - comp_pick)
        sleep(delay)
        print("Remaining " + str(total))
def test_remain():
    """
    Finds the pick number based on the remaining balls.
    If the balls are less than or equal to 4, the user should not pick more than the total.
    :return:
    """
    global pickno
    #Change pick number to the total amount of balls
    # Ex. If we have 3 balls remaining the user cannot pick 4
    if total <= 4:
        pickno = total
def main():
    """
    Runs the Nim game. Asking the user how many balls does he pick. Then calculating the remaining.
    Lets the computer pick. Repeats that till remaining balls are zero. Declares who wins the game.
    :return:
    """
    global user_pick, pickno, total
    test_total()
    sleep(delay)
    print("It is your turn!")
    pickno = int(4)
    #Repeats the process as many times as we need
    while total >= 4:
            user_pick = int(input("How many balls do you want to get? (Up to 4)"))
            test_remain
            test_pick()
            remain()
            cmp_logic()
    sleep(delay)
    print("You should pick " + str(total))
    user_pick = int(input("How many balls do you want to get? (Up to 4)"))
    test_remain()
    test_pick()
    remain()
    # Only way that USER WINS!!
    if int(total) == 0:
        sleep(delay)
        print("User WINS!")
        exit()
main()
