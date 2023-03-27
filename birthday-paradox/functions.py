import datetime, random

def generate_birthdays(number):
    #returns a list of random date objects for birdays
    birthdays = []
    for num in range(int(number)):
        start_date = datetime.date( 2023, 1, 1)
        random_days = datetime.timedelta(random.randint(0,364))
        birthday = start_date + random_days
        birthdays.append(birthday)
    return birthdays

bdays = generate_birthdays(4)
print(bdays)

def check_duplicates(birthdays):
    birthday_set = []
    for a, b in enumerate(birthdays):
        for c, d in enumerate(birthdays[a+1:]):
            if b == d:
                return b
            
            