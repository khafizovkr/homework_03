my_sum = 0
not_quit = True

while not_quit:
    numbers = input('Введите числа через пробел. Для выхода нажмите "q": ')
    numbers = numbers.split()
    for number in numbers:
        if number == 'q':
            not_quit = False
            break
        my_sum += int(number)
    print(my_sum)