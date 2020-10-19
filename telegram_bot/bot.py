import telebot
import config
import random

from telebot import types
from telebot import apihelper

bot = telebot.TeleBot(config.token)
apihelper.proxy = {'https':'socks5://207.154.240.228:9050'}

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/sticker1.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("Не пойти ли вам нахуй?)")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный потому что -".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item3 = types.InlineKeyboardButton("Средне",callback_data='midle')
            item4 = types.InlineKeyboardButton("Отлично, как сам?", callback_data='perfect')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == 'midle':
                bot.send_message(call.message.chat.id, 'Ну и пошел ты нахуй!')
            elif call.data == 'perfect':
                bot.send_message(call.message.chat.id, 'Не выебывайся черт!')


            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)
