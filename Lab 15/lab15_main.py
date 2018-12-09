# Cody Young
# CST 205
# 2018-12-6
# Lab 15
import random
import calendar
from datetime import date
from datetime import datetime

# Problem 1
# Simulates a craps game through dice rolls.

# Helper function that simulates a dice roll.
def dice_roll():
    number = random.randint(1, 7)
    return number

# Runs the craps game.
def crap():
    # Roll two dice and get their sum
    dice_1 = dice_roll()
    dice_2 = dice_roll()
    sum = dice_1 + dice_2

    # Check for win conditions
    if (sum == 7 or sum == 11):
        print("You win!")
    elif (sum == 2 or sum == 3 or sum == 12):
        print("You lose.")
    else:
        point = sum
        dice_1 = dice_roll()
        dice_2 = dice_roll()
        new_sum = dice_1 + dice_2
        print("Rolling...")
        if (new_sum == point):
            print("You win!")
            exit()
        elif (new_sum == 7):
            print("You lose.")
        else:
            print("Try again.")

# Problem 2
# Prints out a monthly calendar.
def month_calendar():
    year = int(input("Enter year:"))
    month = int(input("Enter month:"))

    print(calendar.month(year,month))

# Calculates the number of days until the user's next birthday.
def birthday():
    print("Enter your birth month, day, and the current year.")
    start_year = int(input("Year:"))
    month = int(input("Month:"))
    day = int(input("Day:"))
    current_birthdate = date(start_year, month, day)

    print("Enter the future year and date.")
    end_year = int(input("Year:"))
    end_month = int(input("Month:"))
    end_day = int(input("Day:"))
    end_birthdate = date(end_year, end_month, end_day)

    delta = end_birthdate - current_birthdate

    print(str(delta.days) + " days")

# Outputs when the Declaration of Independence of the United States of America
# was ratified by the Continental Congress.
def freedom_date():

    july_fourth = datetime(1776, 7, 4)

    print("On what date was the Declaration of the Independence of the United States of America ratified by the "
          "Continental Congress?")
    print(july_fourth.strftime("%A %B %w, %Y"))

# Main
def main():
    print("Menu")
    print("1. Craps")
    print("2. Monthly Calendar")
    print("3. Birthday Calculation")
    print("4. Independence Day")
    print("5. Exit")
    uinput = input("Enter selection:")

    if (uinput == "1"):
        crap()
    elif (uinput == "2"):
        month_calendar()
    elif (uinput == "3"):
        birthday()
    elif (uinput == "4"):
        freedom_date()
    elif (uinput == "5"):
        exit()

main()

