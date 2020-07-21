def choice_of_algorithm():
    """
    Функция выбора алгоритма
    :return:
    """
    print(
        '''Введите номер алгоритма:
        1. Сравнение числа с 7
        2. Проверка имени
        3. Проверка массива.
        
        Введите "q" для выхода.''')
    while True:
        try:
            algorithm = input()
            if algorithm == 'q':
                print('Выход из программы.')
                break
            algorithm = int(algorithm)
            if algorithm not in range(1, 4):
                print('Нет алгоритма под этим номером, '
                      'введите число от 1 до 3 или "q" для выхода.')
            else:
                break
        except ValueError:
            print('Введите целое число от 1 до 3 или "q" для выхода.')
    if algorithm == 1:
        check_number()
    elif algorithm == 2:
        check_name()
    elif algorithm == 3:
        check_array()


def is_digit(string):
    """
    Функция проверки на число
    :param string:
    :return: if success: number
             else False
    """
    if string.isdigit():
        return int(string)
    else:
        try:
            number = float(string)
            return number
        except ValueError:
            print('''Некоректный ввод, введите число!''')
            return False


def check_number():
    """
    Алгоритм сравнения числа с 7
    :return:
    """
    print(
        '''Запуск 1 алгоритма
        Введите число.''')
    number = False
    while number is False:
        number = input()
        number = is_digit(number)
    if number > 7:
        print('Привет')


def check_name():
    """
    Алгоритм проверки имени
    :return:
    """
    print(
        '''Запуск 2 алгоритма.
        Введите имя.''')
    name = input()
    if name == 'Вячеслав':
        print('Привет, Вячеслав')
    else:
        print('Нет такого имени')


def check_array():
    """
    Алгоритм вывода чисел кратных 3
    :return:
    """
    print(
        '''Запуск 3 алгоритма.
        Введите последовательность чисел через пробел.''')
    while True:
        try:
            array = input()
            array = array.split()
            if all(is_digit(x) for x in array) and array:
                array = [is_digit(element) for element in array]
                result = [element for element in array if element % 3 == 0]
                print(result)
                break
            else:
                print('''В последовательности чисел ошибка, вводите только числа.''')
        except ValueError:
            print('''Некоректный ввод, попробуйте еще раз.''')


if __name__ == '__main__':
    try:
        choice_of_algorithm()
    except KeyboardInterrupt:
        print('Завершение работы.')
