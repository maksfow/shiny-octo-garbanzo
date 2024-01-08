from telebot import types
bt = types.ReplyKeyboardMarkup(resize_keyboard=True)
rub = types.KeyboardButton("Рубль")
ev = types.KeyboardButton("Евро")
dol = types.KeyboardButton("Доллар")
bt.add(rub,ev,dol)