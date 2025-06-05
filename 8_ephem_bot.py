"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""
### решил немного отойти от задания и сделал поиск значения не через /planet название планеты, а через кнопки из бибилиотеки тг
### понимаю что сообщение /planet Марс можно было разбить через split() и по 1 элементу списка в ф-ции key_reply elif отработать по аналогии
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging,settings,ephem,datetime,re

# Настройки прокси
# PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(filename='bot.log', level=logging.INFO)

planets = {
    'марс': ephem.Mars(),
    'юпитер': ephem.Jupiter()
    }

current_date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет')

def planet_user(update, context):
    planet_key = [['Марс'],['Юпитер'],
                  ['Закрыть список']]
    view_keyboard = ReplyKeyboardMarkup(planet_key, resize_keyboard=True)
    update.message.reply_text('Выберите планету', reply_markup = view_keyboard)

def key_reply(update, context):
    user_messg = update.message.text.lower()
    if user_messg == 'закрыть список':
        update.message.reply_text('Список закрыт', reply_markup=ReplyKeyboardRemove())
        return
    
    elif user_messg in planets:
        planet = planets[user_messg]
        planet.compute(current_date)
        constellation = ephem.constellation(planet)[1]
        update.message.reply_text(f'Планета {user_messg.capitalize()} на момент {current_date} находится в созвездии {constellation}')
    else:
        update.message.reply_text('Планета не найдена')

# def talk_to_me(update, context):
#     user_text = update.message.text 
#     print(user_text)
#     update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_user))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), key_reply))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()

    mybot.idle()

if __name__ == "__main__":
    main()

