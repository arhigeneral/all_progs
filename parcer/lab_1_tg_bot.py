import telebot
import config
import parcer

from telebot import types
from telebot import apihelper

bot = telebot.TeleBot(config.token)
apihelper.proxy = {'https':'socks5://207.154.240.228:9050'}

@bot.message_handler(commands=['start'])
def welcome(message):


    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Статьи на хабре")
    item2 = types.KeyboardButton("Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный потому что - надо сдать 1 лабу!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Статьи на хабре':
            bot.send_message(message.chat.id, "По какому ключевому слову найти статью?")
        elif message.text == 'Как дела?':
            # Переделать эту кнопку потом
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text != 'Статьи на хабре':
            bot.send_message(message.chat.id, parcer.articles(message.text)[0])
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает')


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
