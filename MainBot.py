# bot TestSeminar
import telebot
import random
from telebot import types
import Compress
import Decompress
from TOKEN import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    text_message = f'<b><i> Привет {message.from_user.first_name}! </i></b> \U0001F600'
    # \U0001F600 - выводит смайлик, {message.from_user.first_name} - выводит имя пользователя
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    item1 = types.KeyboardButton('Знак зодиака')
    item2 = types.KeyboardButton('Угадайка')
    item3 = types.KeyboardButton('Сжать текст')
    item4 = types.KeyboardButton('Раскрыть текст')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, text_message, parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, 'Выберите задачу')
@bot.message_handler(content_types=['text'])
def f(message):
    if message.text == 'Знак зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item_1 = telebot.types.InlineKeyboardButton('овен', callback_data='овен')
        item_2 = telebot.types.InlineKeyboardButton('козерог', callback_data='козерог')
        item_3 = telebot.types.InlineKeyboardButton('водолей', callback_data='водолей')
        item_4 = telebot.types.InlineKeyboardButton('стрелец', callback_data='стрелец')
        item_5 = telebot.types.InlineKeyboardButton('рак', callback_data='рак')
        item_6 = telebot.types.InlineKeyboardButton('дева', callback_data='дева')
        item_7 = telebot.types.InlineKeyboardButton('близнецы', callback_data='близнецы')
        item_8 = telebot.types.InlineKeyboardButton('скорпион', callback_data='скорпион')
        item_9 = telebot.types.InlineKeyboardButton('весы', callback_data='весы')
        item_10 = telebot.types.InlineKeyboardButton('телец', callback_data='телец')
        item_11 = telebot.types.InlineKeyboardButton('рыбы', callback_data='рыбы')
        item_12 = telebot.types.InlineKeyboardButton('лев', callback_data='лев')
        markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12)
        bot.send_message(message.chat.id, 'Отлично, нажимай!', reply_markup=markup)
    elif message.text == 'Угадайка':
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
        num_01 = telebot.types.InlineKeyboardButton('Загадать число', callback_data='Загадать число')
        num_02 = telebot.types.InlineKeyboardButton('Угадать число', callback_data='Угадать число')       
        keyboard.add(num_01, num_02)
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboard) # replay_markup=keyboard - запускает кнопки
    elif message.text == 'Сжать текст':
        bot.send_message(message.chat.id, 'Введите строку для сжатия')
        bot.register_next_step_handler(message, send_RLS)
    elif message.text == 'Раскрыть текст':
        bot.send_message(message.chat.id, 'Введите строку для раскрытия')
        bot.register_next_step_handler(message, send_DC)
def input(message):
    str_out = message.text
    return str_out
def send_RLS(message):
    input_str = message.text
    bot.send_message(message.chat.id, str(Compress.Compress(input_str)))

def send_DC(message):
    input_str = message.text
    bot.send_message(message.chat.id, str(Decompress.Decompress(input_str)))
def get_number():
    global x
    x = str(random.randint(1, 5))
    return x
def str_compress(message):
    result = message.text
    bot.send_message(message.chat.id, Compress.Compress(result))    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    dikt_znak = znak_har()
    if call.data == 'овен':
        bot.send_message(call.message.chat.id, dikt_znak['овен'])
    elif call.data == 'телец':
        bot.send_message(call.message.chat.id, dikt_znak['телец'])
    elif call.data == 'козерог':
        bot.send_message(call.message.chat.id, dikt_znak['козерог'])
    elif call.data == 'лев':
        bot.send_message(call.message.chat.id, dikt_znak['лев'])
    elif call.data == 'рыбы':
        bot.send_message(call.message.chat.id, dikt_znak['рыбы'])
    elif call.data == 'скорпион':
        bot.send_message(call.message.chat.id, dikt_znak['скорпион'])
    elif call.data == 'близнецы':
        bot.send_message(call.message.chat.id, dikt_znak['близнецы'])
    elif call.data == 'весы':
        bot.send_message(call.message.chat.id, dikt_znak['весы'])
    elif call.data == 'рак':
        bot.send_message(call.message.chat.id, dikt_znak['рак'])
    elif call.data == 'дева':
        bot.send_message(call.message.chat.id, dikt_znak['дева'])
    elif call.data == 'водолей':
        bot.send_message(call.message.chat.id, dikt_znak['водолей'])
    elif call.data == 'стрелец':
        bot.send_message(call.message.chat.id, dikt_znak['стрелец'])
    elif call.data == 'Загадать число':
        get_number()
        bot.send_message(call.message.chat.id, 'Число загадано от 1 до 5!')
    elif call.data == 'Угадать число':
        bot.send_message(call.message.chat.id, 'Введите предпологаемое число')
        bot.register_next_step_handler(call.message, input_num)
    elif call.data == 'Сжать текст':
        send_RLS(call.message)
    elif call.data == 'Раскрыть текст':
        send_DC(call.message)
def input_num(message):
    num = message.text
    if x == num:
        bot.send_message(message.chat.id, 'Вы угадали!!!')
        bot.send_message(message.chat.id, 'Можете выбрать задачу повторно')
    else:
        bot.send_message(message.chat.id, 'Попробуйте еще раз!')
        bot.register_next_step_handler(message, input_num)        
def znak_har():
    dict = {}
    with open('text2.txt', 'r', encoding='utf-8') as file:
        for i in range(12):
            str1 = file.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
    return dict

print('Bot is started')
bot.polling(non_stop=True)