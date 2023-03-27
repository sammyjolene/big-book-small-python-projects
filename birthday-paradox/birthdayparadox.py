# Birthday Paradox, by Al Sweigart al@inventwithpython.com

from functions import generate_birthdays, check_duplicates
import datetime, random

number_of_birthdays = input("How many birthdays should I create?")

print("Here are ", number_of_birthdays, " birthdays.")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
birthdays = generate_birthdays(number_of_birthdays)
# print(birthdays)
for i, bday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = months[bday.month-1]
    dateText = '{} {}'.format(month_name, bday.day)
    print(dateText, end='')

match = check_duplicates(birthdays)
print(match)