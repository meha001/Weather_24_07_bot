import telebot
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API = os.getenv("API")

load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")


bot = telebot.TeleBot(TOKEN_BOT)

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


#el,l;,l;lms;mdlml;vmlmmldsml;vml;smv;lms;vm;lsmv s;lvmlsm;lvmslmvms;lvm;lsmvlms;lmvv
