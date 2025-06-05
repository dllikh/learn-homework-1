"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break   
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    dictionary_list = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
    user_mess = ''
    while True:
        try:
            if user_mess != 'Закончить':
                    user_mess = input('Задайте вопрос\n')
                    if user_mess in dictionary_list:
                        print(dictionary_list[user_mess])
                        user_mess = input('Задайте вопрос, либо введите "Закончить"\n')
                    else:
                        input('Задайте вопрос, либо введите "Закончить"\n')
        except KeyboardInterrupt:
            print('Пока!')
            break
        
if __name__ == "__main__":
    ask_user()
