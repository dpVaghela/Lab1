#!/usr/bin/env python3

from datetime import datetime

def calculate_age(birth_year):
    present_year = datetime.now().year
    age = present_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print("Your age is:", age)