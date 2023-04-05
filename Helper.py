import random
import datetime

names = ['John', 'Mohamed', 'Michel', 'Sam',
         'Mark', 'Ramy', 'Waleed', 'Hossam', 'Abdo', 'Noor',
         'Karim', 'Samy', 'Youssef', 'Elon',
         'Ahmed', 'Hossam', 'Samy', 'Mona',
         'Mariam', 'Walaa', 'Sohila', 'Samir'
         ]


def generate_age(s=10, e=90):
    # SETTING LIMITS #
    s = max(s, 5)
    e = min(e, 110)

    return random.randint(10, 90)


def generate_name():
    first_name = random.randint(1, len(names) - 1)
    second_name = random.randint(1, len(names) - 1)
    name = names[first_name] + ' ' + names[second_name]

    # Formatting the name to be all the same length
    space_left = 20 - len(name)
    space_left = (' ' * space_left)
    name += space_left

    return name


def generate_phone_number():  # Egyptian Number
    numbers = ['5', '2', '1', '0']
    number = '01'

    number += str(numbers[random.randint(0, len(numbers) - 1)])
    for i in range(8):
        number += str(random.randint(0, 9))

    return number


def generate_date():
    start_date = datetime.date(1850, 1, 1)  # start of range
    end_date = datetime.date(2023, 12, 31)  # end of range

    # generate a random number of days between start and end
    delta = random.randint(0, (end_date - start_date).days)

    # add the random number of days to the start date to get a random date
    random_date = start_date + datetime.timedelta(days=delta)

    return random_date
