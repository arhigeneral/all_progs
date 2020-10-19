import telebot
import config
import parcer

from telebot import types
from telebot import apihelper

bot = telebot.TeleBot(config.token)
apihelper.proxy = {'https':'socks5://88.202.177.242:1090'}

@bot.message_handler(commands=['start'])
def welcome(message):


    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Статьи на хабре")

    markup.add(item1)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный потому что - надо сдать 1 лабу!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Статьи на хабре':
            bot.send_message(message.chat.id, "По какому ключевому слову найти статьи?")
            global marker
            marker = 21
        elif message.text != 'Статьи на хабре' and marker == 21:
            marker -= 1
            for i in range (0, len(parcer.articles(message.text))):
                bot.send_message(message.chat.id, parcer.articles(message.text)[i])
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')


# RUN
bot.polling(none_stop=True)
