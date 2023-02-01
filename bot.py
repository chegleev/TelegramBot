import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def blalala (message):
    key = types.ReplyKeyboardMarkup (resize_keyboard = True)
    button_1 = types.KeyboardButton ("Ice cream")
    button_2 = types.KeyboardButton ("Meat")
    button_3 = types.KeyboardButton ("Beer")
    key.add (button_1, button_2)
    key.add (button_3)
    bot.send_message (message.chat.id, 'What tastes better?', reply_markup = key)

@bot.message_handler (content_types=['text'])
def hohoho (message):
    markup_inline = types.InlineKeyboardMarkup ()
    if message.text == 'Ice cream':
        bot.send_message (message.chat.id, "I love ice cream too!", reply_markup=markup_inline)
    elif message.text == 'Meat':
        bot.send_message (message.chat.id, "I don't like meat, I'm a vegetarian!", reply_markup=markup_inline)
    elif message.text == 'Beer':
        bot.send_message (message.chat.id, "I do not like beer!, reply_markup=markup_inline)
    else:
        bot.send_message (message.chat.id, "Incorrect message!", reply_markup=markup_inline)
    print(message.text)

bot.infinity_polling()
