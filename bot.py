import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def blalala (message):
    key = types.ReplyKeyboardMarkup (resize_keyboard = True)
    button_1 = types.KeyboardButton ("Мороженое")
    button_2 = types.KeyboardButton ("Шашлык")
    button_3 = types.KeyboardButton ("Пиво")
    key.add (button_1, button_2, button_3)
    bot.send_message (message.chat.id, 'Что вкуснее?', reply_markup = key)

@bot.message_handler (content_types=['text'])
def hohoho (message):
    markup_inline = types.InlineKeyboardMarkup (row_width = 3)
    if message.text == 'Мороженое':
        bot.send_message (message.chat.id, "Тоже его обожаю 😍😍😍", reply_markup=markup_inline)
    elif message.text == 'Шашлык':
        bot.send_message (message.chat.id, "Не ем мясо 🤮 , я веган!", reply_markup=markup_inline)
    elif message.text == 'Пиво':
        bot.send_message (message.chat.id, "Сейчас нет настоящего пива, всё химия ☝️😏", reply_markup=markup_inline)
    else:
        bot.send_message (message.chat.id, "Чёт не то ты мне прислал 🤔", reply_markup=markup_inline)
    print(message.text)

bot.polling(none_stop=True)