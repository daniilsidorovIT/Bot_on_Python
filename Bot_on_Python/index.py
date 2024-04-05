# ID BOTS IN TELEGRAMM - Bot_Happy23_bot

import telebot
from telebot import types

photo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkT5HDfBWfgP-XAqCJGbvI3Cn0v7YSuCGbEWHp6CxoPA&s'
token = '7040706306:AAH0VJ_nYwXiqmWEErOYoXGl3agtI8iPupc'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton('Отправить картинку'),types.KeyboardButton('Отправить файл'))
    keyboard.add(types.KeyboardButton('Ответить на вопрос'))
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!', reply_markup=keyboard)
    
    
@bot.message_handler(content_types=['text'])  
def main_menu(message):
    if message.text == 'Отправить картинку':
        bot.send_photo(message.chat.id, photo=photo_url, caption='Это собака!')
    elif message.text == 'Отправить файл':
        f = open ('file.txt', 'rb')
        bot.send_document(message.chat.id, document=f, caption='Очень важный файл')
    elif message.text == 'Ответить на вопрос':
        inlineKeyboard = types.InlineKeyboardMarkup()
        inlineKeyboard.add(types.InlineKeyboardButton('2', callback_data='2'))
        inlineKeyboard.add(types.InlineKeyboardButton('4', callback_data='4'))
        inlineKeyboard.add(types.InlineKeyboardButton('5', callback_data='5'))
        bot.send_message(message.chat.id, '2+2=?', reply_markup=inlineKeyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def getAnswer(call):
    if call.data == '4':
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Вы ответили верно!')
    else:
        bot.send_message(call.message.chat.id, 'Ответ неверный, попробуйте снова (')
    bot.answer_callback_query(call.id)
bot.polling(non_stop=True)


