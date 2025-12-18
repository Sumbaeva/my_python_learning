import math


def square(side):
    area = side * side
    # Если сторона не целая, округляем результат вверх (ceil).
    if not isinstance(side, int):
        area = math.ceil(area)
    return area
