"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [
        {'school_class': '4а', 'scores': [3,4,4,5,2]},
        {'school_class': '4б', 'scores': [5,4,3,3,4]},
        {'school_class': '4в', 'scores': [3,3,3,3,4]}
    ]
    total_class = 0
    amount_score = 0
    for score in data:
        summ_class = sum(score['scores'])
        total_class += summ_class
        amount_score += len(score['scores'])
        print(f'Средняя оценка сласса {score['school_class']} = {summ_class/len(score['scores'])}')
    print(f"Средний балл по всей школе = {round(total_class/amount_score,2)}")
if __name__ == "__main__":
    main()
