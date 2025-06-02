# Домашка номер 3!
"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

phones =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main(phones):
    total_sold = 0
    avg_total_sold = 0
    for sum_sold in phones:
        sum_sold['all_sold'] = sum(sum_sold['items_sold'])
        print(f'Суммарное количество продаж для {sum_sold['product']} - {sum_sold['all_sold']}')
        avg_sold = sum_sold['all_sold']/len(sum_sold['items_sold'])
        print(f'Среднее количество продаж для {sum_sold['product']} - {round(avg_sold,2)}')
        total_sold += sum_sold['all_sold']
        avg_total_sold += avg_sold
    print(f'Суммарное количество продаж для всех товаров - {total_sold}')
    print(f'Среднее количество продаж всех товаров - {round(avg_total_sold,2)}')
            
    
    
if __name__ == "__main__":
    main(phones)
