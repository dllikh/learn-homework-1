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
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    first_line = 1
    second_line = 'learn'
    if type(first_line) != str or type(second_line) != str:
        num_response = 0
    elif first_line == second_line:
        num_response = 1
    elif len(first_line) > len(second_line):
        num_response = 2
    elif first_line != second_line and second_line == 'learn':
        num_response = 3
    return num_response
    
if __name__ == "__main__":
    print(main())
