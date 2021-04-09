import datetime
from random import choice, randrange, randint

from annoy_scammers.helpers import rand_int, rand_letters


def get_name():
    f_names = open('firstnames.txt', 'r').read().split('\n')
    l_names = open('lastnames.txt', 'r').read().split('\n')
    first = choice(f_names)
    last = choice(l_names)

    return f"{first} {last}"


def get_phone_number():
    return '07' + str(rand_int(9))


def get_dob():
    start_date = datetime.date(1940, 1, 1)
    end_date = datetime.date(2000, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date.strftime('%d / %m / %Y')


def get_postcode():
    return f"{rand_letters(2)}{str(rand_int(1))} {str(rand_int(1))}{rand_letters(2, 'CIKMOV')}"


def get_address():
    words = open('words.txt', 'r').read().split('\n')
    filtered_words = [w for w in words if len(w) >= 3]
    street_names = [w for w in filtered_words if w[0].isupper() and w[1:].islower()]
    suffixes = ['Road', 'Street', 'Lane', 'Avenue', 'Drive']

    return f"{str(randint(1, 150))} {choice(street_names)} {choice(suffixes)}"


def get_card_number(length=16):
    card_number = choice(['4', '5']) + str(rand_int(length - 2))
    sum_sum_digits = 0
    for i in range(len(card_number)):
        if not i % 2:
            double = int(card_number[i]) * 2
            for d in str(double):
                sum_sum_digits += int(d)
        else:
            sum_sum_digits += int(card_number[i])
    checksum = sum_sum_digits * 9 % 10
    card_number += str(checksum)
    return " ".join(card_number[i:i + 4] for i in range(0, len(card_number), 4))


def get_expiry_date():
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now() + datetime.timedelta(days=365 * 3)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date.strftime('%m / %y')


def get_cvv():
    return str(rand_int(3))


def get_account_number():
    return str(rand_int(8))


def get_sort_code():
    return f"{rand_int(2)}-{rand_int(2)}-{rand_int(2)}"
