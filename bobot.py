import os
from random import choice
from telebot import TeleBot, types


TOKEN = '7151982102:AAGpEHhkRh5cjp2GNvMB5Mt8vwWgpaXcah4'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['meme'])
def start(message):
    file = choice(os.listdir('images'))
    with open(f'images/{file}', 'rb') as f:
        bot.send_photo(message.chat.id, photo=f)

if __name__ == '__main__':
    bot.polling(none_stop=True)