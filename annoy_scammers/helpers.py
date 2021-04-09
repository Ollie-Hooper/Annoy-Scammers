import string
from random import randint, choices


def rand_int(digits=1):
    return randint(10 ** (digits - 1), int(''.join(['9' for i in range(digits)])))


def rand_letters(length, exceptions=''):
    return "".join(choices([c for c in string.ascii_uppercase if c not in exceptions], k=length))
