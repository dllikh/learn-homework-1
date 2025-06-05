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
#Сделал немного по другому, не деленеем строки и вызовом /planet название планеты, а через кнопки в самом тг боте
import logging, ephem, settings, datetime
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = "Вызван /start"
    print(text)
    update.message.reply_text(text)

def planet_user(update, context):
    planet_keyboard = [["Mars", "Jupiter"]]
    reply_markup = ReplyKeyboardMarkup(planet_keyboard, resize_keyboard=True)
    update.message.reply_text("Выберите планету:", reply_markup=reply_markup)

def key_reply(update, context):
    key_text = update.message.text.lower()
    current_date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    planets = {
        'mars': ephem.Mars(),
        'jupiter': ephem.Jupiter(),
    }
    if key_text in planets:
        planet = planets[key_text]
        planet.compute(current_date)
        constellation = ephem.constellation(planet)[1]
        update.message.reply_text(f"Планета {key_text.capitalize()} на момент {current_date} находится в созвездии {constellation}")
    else:
        update.message.reply_text("Задано неверное условие",reply_markup=ReplyKeyboardRemove())
        
def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_user))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command),key_reply))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()