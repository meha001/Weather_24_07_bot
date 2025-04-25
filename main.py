import telebot
import requests
import json

API = '61707cade23979320ec02eb97108c139'

bot = telebot.TeleBot("7630130715:AAFiLkBzSaRFvRjzhHmp5YYK9m9UFCd0-mI")

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, рад тебя видеть! Напиши название города")

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        image = "1.jpg" if temp > 5.0 else "2.jpg" 
        bot.reply_to(message, f'Сейчас погода: {temp}')
        file = open(image, "rb")
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Название города указан неверно")

bot.polling(none_stop = True)

