"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
"""


def ask_user():
    """
    Замените pass на ваш код
    """

    user_mess = input('Как дела?\n')
    while user_mess != 'Хорошо':
        user_mess = input('Как дела?\n')
    print('Цикл завершен')

   
if __name__ == "__main__":
    ask_user()
