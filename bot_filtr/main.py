from telebot import TeleBot
from random import choice
import json




TOKEN = 'ваш TOKEN'
bot = TeleBot('6417878287:AAGLcUU4lv1V1-Ahhroqqgm3aFJuAxcmRwg')




game = False
used_words = []
letter = ''
points = 0
leaderboard = {}




with open('cities.txt', 'r', encoding='utf-8') as f:
    cities = [line.strip().lower() for line in f.readlines()]




def select_letter(word):
    i = -1
    while word[i] in ('й', 'ь', 'ы', 'ъ'):
        i -= 1
        return word[i]




@bot.message_handler(commands=['leaderboard'])
def leaderboard(message):
    with open('scores.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    leaders_str = ''
    for user, user_points in data.items():
        leaders_str += user + ' ' + str(user_points) + '/n'
    bot.send_message(message.chat.id, text=leaders_str)




@bot.message_handler(commands=['save'])
def save(message):
    with open('scores.json', 'w', encoding='utf-8') as f:
        json.dump(leaderboard, f)
    bot.send_message(message.chat.id,  'Прогресс сохранен')




@bot.message_handler(commands=['goroda'])
def goroda(message):
    global game, letter
    game = True
    city = choice(cities)
    letter = select_letter(city)
    bot.send_message(message.chat.id, city)




@bot.message_handler()
def game (message):
    global used_words, letter, game, points
    if game:
        if message.text.lower() in used_words:
            print(letter)
            bot.send_message(message.chat.id, ' уже было')
            return
        if message.text.lower()[0] != letter:
            bot.send_message(message.chat.id, 'заткнись уже')
            return
        if message.text.lower() in cities:
            if message.from_user.first_name in leaderboard:
                leaderboard[message.from_user.first_name] += 1
            else:
                leaderboard[message.from_user.first_name] = 1
            letter = select_letter(message.text.lower())
            used_words.append(message.text.lower())
            for city in cities:
                if city[0] == letter and city not in used_words:
                    letter = select_letter(city)
                    bot.send_message(message.chat.id, city)
                    used_words.append(city)
                    return
                bot.send_message(message.chat.id, 'гг')
                game = False
                return
            bot.send_message(message.chat.id, 'лее падла')




if __name__ == '__main__':
    bot.polling(none_stop=True)






