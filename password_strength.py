#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import getpass
import requests

def check_number(password):
    return bool(re.findall(r'[0-9]', password))

def check_upper(password):
    return bool(re.findall(r'[A-Z]', password))

def check_lower(password):
    return bool(re.findall(r'[a-z]', password))

def check_special(password):
    return bool(re.findall(r'[!@#$%&?_]', password))

def check_repeating(password):
    return re.findall(r'(.)\1{2,}', password)

def check_year(password):
    for year in range(1930,2019):
        if str(year) in password:
            return True

def get_password_blacklist():
    blacklist_url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_10000.txt'
    blacklist = requests.get(blacklist_url)
    print(blacklist.split('\r\n'))

def compile_blacklist():
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
    blacklist_compiled = [re.compile(bl) for bl in blacklist]
    return blacklist_compiled


def set_password_strength(password):

    password_strength = dict.fromkeys([
        'not_in_blacklist',
        'has_special',
        'has_upper',
        'has_lower',
        'has_num',
        'has_no_date',
        ], False)

    bl_match = compile_blacklist()

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
    print(password, password_strength.values())
    if password_strength['not_in_blacklist'] is True:
        score = len([b for b in password_strength.values() if b])
        if not all([password_strength[key] is True for key in
           password_strength.keys()][2:5]):
            print(score)
            return round(score * 1.33)
        if password[-1].isdigit():
            print(score)
            return round(score * 1.22)
        else:
            print(score)
            return round(score * 1.66)
    else:
        score = 1
        return score


def main():
    print('Enter a password.\n\n'
          'The password must be between 6 and 12 characters.\n')

    while True:
        password =  getpass.getpass(prompt= 'Password: ')
        print(password)
        print(len(password))
        if 6 <= len(password) <= 12:
            break
        print('\nWARNING: The password must be between 6 and 12 characters.\n')

    score = get_password_strength(password)
    print('Your password score is {0}'.format(score))
    print(get_password_blacklist())


if __name__ == '__main__':
    main()
