import random
from math import sqrt, ceil

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_number():
    return random.randint(0, 1000)


def is_2_or_3(number):
    return number == 2 or number == 3


def is_divisible_by(number, divider):
    return number % divider == 0


def is_prime(number):
    if number < 2:
        return False
    ceil_least_divider = ceil(sqrt(number))
    for divider in range(2, ceil_least_divider + 1):
        if is_divisible_by(number, divider):
            return False
    return True


def make_question_answer():
    number = generate_number()
    right_answer = is_prime(number)
    return str(number), 'yes' if right_answer else 'no'
