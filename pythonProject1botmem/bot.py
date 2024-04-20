import pickle
from random import choice
from telebot import TeleBot, types

TOKEN = '6417878287:AAGLcUU4lv1V1-Ahhroqqgm3aFJuAxcmRwg'
bot = TeleBot(TOKEN)


with open('aneks.pickle', 'r') as f:
    data = pickle.load(f)

@bot.message_handler(func=lambda call: call.data)
def send_anek(call):
    anek = choice(data[call.data])
    bot.send_message(call.message.chat.id, text=anek)

@bot.message_handler()
def start(message):
    markup = types.InlineKeyboardMarkup()
    for category in data.keys():
        markup.add(types.InlineKeyboardButton(category, callback_data=category))
        bot.send_message(
        message.chat.id, text='Выберите категорию', reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
