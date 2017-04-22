#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


def set_password_strength(password):
    password_strength = dict.fromkeys([
        'not_in_blacklist',
        'has_special',
        'has_upper',
        'has_lower',
        'has_num',
        'has_no_date',
        ], False)

    # character repeating stands for r'(.)\1{4,}'

    blacklist = [
        r'(.)\1{4,}',
        '123',
        '5678abc',
        'qwer',
        'asdf',
        'Passw',
        'Qwer',
        '1q2w3e',
        '9876',
        '5432',
        'pass',
        ]
    bl_match = [re.compile(bl) for bl in blacklist]

    if not any(p.match(password) for p in bl_match):
        password_strength['not_in_blacklist'] = True
    if re.search(r'[!@#$%&?_]', password):
        password_strength['has_special'] = True
    if re.search(r'[A-Z]', password):
        password_strength['has_upper'] = True
    if re.search(r'[a-z]', password):
        password_strength['has_lower'] = True
    if re.search(r'[0-9]', password):
        password_strength['has_num'] = True
        if (not re.search(r'^(19|20)\d{2}', password) and
                not re.search(r'[0-9]{4}$', password)):
                    password_strength['has_no_date'] = True
    return password_strength


def get_password_strength(password):
    password_strength = set_password_strength(password)
    if password_strength['not_in_blacklist'] is True:
        score = len([b for b in password_strength.values() if b])
        if not all([password_strength[key] is True for key in
           password_strength.keys()][2:5]):
            return round(score * 1.33)
        if password[-1].isdigit():
            return round(score * 1.22)
        else:
            return round(score * 1.66)
    else:
        score = 1
        return score


def main():
    print('Enter a password.\n\n'
          'The password must be between 6 and 12 characters.\n')

    while True:
        password = input('Password: ')
        if 6 <= len(password) < 12:
            break
        print('\nWARNING: The password must be between 6 and 12 characters.\n')

    score = get_password_strength(password)
    print('Your password score is {0}'.format(score))


if __name__ == '__main__':
    main()
