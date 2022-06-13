# Phone number validation
# 1. Only digits are allowed
# 2. Starts with 1,8,9
# 3. May contain only 8 digits
import re


def check_first_dig(number):
    pattern = r"^[1,8,9]"
    if re.search(pattern, number):
        return True
    else:
        global result
        result = result + "The first digit must be 1,8 or 9 only. Try again."
        return False


def check_length(number):
    if len(number) == 8:
        return True
    else:
        global result
        result = result + "Exactly 8 digits is needed. Try again"
        return False


def is_digit(number):
    if number.isdigit():
        return True
    else:
        global result
        result = result + "Only digits are acceptable. Try again"
        return False


def validator(number):
    if not check_length(num) or not check_first_dig(num) or not is_digit(num):
        print(result)
    else:
        global progress
        progress = False
        print("Accepted!")


progress = True
while progress:
    result = "There is a problem: "
    num = input("Input phone number: ")
    validator(num)
