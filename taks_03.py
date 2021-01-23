#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(num_1, num_2, num_3):
    return num_1 + num_2 + num_3 - min(num_1, num_2, num_3)


print(my_func(500, 500, 500))
print(my_func(5, 500, 65))
print(my_func(5, 14, 65))
print(my_func(1000, 500, 65))