# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.
def user_info(name, surname, date_of_birth, city, email, phone):
    print(f'User info: {name}, {surname}, {date_of_birth}, {city}, {email}, {phone}')


user_info(name='Ivan', date_of_birth=1994, email='ivan@gmail.com', city='Moscow', phone='123456', surname='Ivanov')
