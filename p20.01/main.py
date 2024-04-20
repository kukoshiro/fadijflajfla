from telebot import TeleBot
from time import time
from random import randint

bot = TeleBot('6417878287:AAGLcUU4lv1V1-Ahhroqqgm3aFJuAxcmRwg')

with open('bad_words.txt', 'r', encoding='utf-8') as f:
    data = [word.strip().lower() for word in f.readlines()]

def is_group(message):
    return message.chat.type in ('group', 'supergroup')

@bot.message_handler(func=lambda message: message.entities is not None and is_group(message))
def delete_links(message):
    for entity in message.entities:
        if entity.type in ['url', 'text_link']:
            bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: message.text.lower() in data and is_group(message))
def bad_word(message):
    bot.restrict_chat_member(
        message.chat.id,
        message.from_user.id,
        until_date=time()+600)

    bot.send_message(message.chat.id, text='дура старая', reply_to_message_id=message.message_id)

    bot.delete_message(message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling(non_stop=True)