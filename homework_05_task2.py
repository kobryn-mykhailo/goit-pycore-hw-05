# Homework 05 - Task 2
# Generator function to extract real numbers from text and calculate total profit.

import re
from typing import Callable


def generator_numbers(text: str):
    # Generator that parses text and yields all real numbers
    # that are clearly separated by spaces on both sides.
    pattern = r'(?<= )\d+\.\d+(?= )'
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    # Calculates total sum of all real numbers in text
    # using the provided generator function.
    return sum(func(text))


# Example usage
if __name__ == "__main__":
    text = ("Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими надходженнями "
            "27.45 і 324.00 доларів.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")