import telebot

bot = telebot.TeleBot("6832959280:AAEr_m3DPjkw6yj_DSuukDpS4KaSDYKSPhM")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(commands=['givemoney'])
def main(message):
    bot.send_message(message.chat.id, "Выдано - 1000$.")


@bot.message_handler(commands=['police'])
def main(message):
    bot.send_message(message.chat.id, "Вы вызвали полицию на свой IP адрес.")


bot.infinity_polling()