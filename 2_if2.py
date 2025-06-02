"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(first_line,second_line):
    first_type = type(first_line)
    second_type = type(second_line)
    if first_type != str or second_type != str:
        value = 0
    else:
        if first_line == second_line:
            value = 1
        else:
            if len(first_line) > len(second_line):
                value = 2
            elif second_line == 'learn':
                value = 3
            else:
                value = 'Не существует условий, при которых вторая строка длиннее первой!'
    return value

first_line = input('Введите первую строку : ')
second_line = input( 'Введите вторую строку : ')


if __name__ == "__main__":
    print(main(first_line,second_line))
