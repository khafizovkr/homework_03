def my_func(x, y):
    return x ** y


print(my_func(5, 0))

def my_func1(x, y):
    s = 1
    for i in range(abs(y)):
        s *= x
    return 1 / s if y < 0 else s


print(my_func1(5, -2))