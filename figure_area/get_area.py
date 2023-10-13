import math
import warnings


def positive_arguments_decorator(func):
    def full_check(*args):
        all_arguments_not_negative = all([arg > 0 for arg in args])
        return func(*args) if all_arguments_not_negative \
            else warnings.warn('All arguments must be greater than zero')
    return full_check


@positive_arguments_decorator
def circle(radius: int | float):
    """
    Вычисляет площадь круга по радиусу.
    """
    return math.pi * radius**2


@positive_arguments_decorator
def triangle(side1: int | float, side2: int | float, side3: int | float):
    """
    Вычисляет площадь треугольника по трём сторонам.
    """
    p = (side1 + side2 + side3) / 2
    return math.sqrt(p * (p - side1) * (p - side2) * (p - side3))

