import requests
import telebot
from telebot.types import ReplyKeyboardRemove
from фф import bt

bot = telebot.TeleBot("6869373189:AAF1t8p9yf4YrptHbACrSm1TxA_YV6McwnQ")

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Добро пожаловать в конвертор валют!\nВыберите валюту: ",reply_markup=bt)
@bot.message_handler(content_types=['text'])
def text_message(message):
    user_id = message.from_user.id
    if message.text == "Рубль":
        bot.send_message(user_id, "Введите сумму, которую необходимо перевести в рубль: ", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, rub)
    elif message.text == "Евро":
        bot.send_message(user_id, "Введите сумму, которую необходимо перевести в евро: ", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ev)
    elif message.text == "Доллар":
        bot.send_message(user_id, "Введите сумму, которую необходимо перевести в доллар: ", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, dol)
while True:
 def rub(message):
    mess = float(message.text)
    ress = 0.0074*mess
    user_id = message.from_user.id
    bot.send_message(user_id,ress)
 def ev(message):
    mess = float(message.text)
    ress = 0.000074*mess
    user_id = message.from_user.id
    bot.send_message(user_id,ress)
 def dol(message):
    mess = float(message.text)
    ress = 0.000081*mess
    user_id = message.from_user.id
    bot.send_message(user_id,ress)

 bot.polling(non_stop=True)