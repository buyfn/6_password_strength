import string
import re
import os
import sys

from dateutil.parser import parse


def load_blacklist():
    current_directory = os.getcwd()

    try:
        filepath = os.path.join(current_directory, sys.argv[1])
    except IndexError:
        return []

    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as file_handler:
        return file_handler.read().split()


def contains_any(s, charset):
    for char in s:
        if char in charset:
            return True
    return False


def contains_upper_and_lower(password):
    return contains_any(password, string.ascii_uppercase) and \
           contains_any(password, string.ascii_lowercase)


def contains_digit_and_letter(password):
    return contains_any(password, string.digits) and \
           contains_any(password, string.ascii_letters)


def contains_special(password):
    special_chars = "!@#$%^&*"
    return contains_any(password, special_chars)


def is_date(password):
    try:
        parse(password)
        return True
    except ValueError:
        return False


def is_license_plate(password):
    def matches(pattern):
        search_obj = re.search(pattern, password)
        if search_obj:
            return search_obj.group() == password
        else:
            return False

    patterns = ['[a-z]{1}[0-9]{3}[a-z]{2}[0-9]{2,3}',  # russian
                '[0-9]{4}[a-z]{2}-?[0-9]{1}']          # belarussian

    return any([matches(pattern) for pattern in patterns])


def prohibited(password, blacklist):
    return any([password in blacklist,
                is_date(password),
                is_license_plate(password)])


def get_password_strength(password, blacklist=[]):
    strength = 1

    # points for length
    if len(password) > 10:
        strength = 4
    elif len(password) > 6:
        strength = 2

    # points for passing requirements
    rules = [contains_upper_and_lower,
             contains_digit_and_letter,
             contains_special]
    for rule in rules:
        if rule(password):
            strength += 2

    if prohibited(password, blacklist):
        return 1
    else:
        return min(10, strength)


if __name__ == '__main__':
    blacklist = load_blacklist()
    password = input('Enter a password: ')
    print('Password strength: {}'.format(get_password_strength(password,
                                                               blacklist)))
