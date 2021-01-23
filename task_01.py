# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.
number_1 = int(input('Введите делимое: '))
number_2 = int(input('Вдедите делитель: '))


def divide(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return 'Деление на ноль'


print(divide(number_1, number_2))
