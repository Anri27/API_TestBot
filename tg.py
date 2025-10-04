import telebot
import os
import requests
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN1")
WEATHER_TOKEN =os.getenv("WEATHER_TOKEN1") 


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def command_start(message):
    bot.reply_to(message, "Напиши название любого города.")



@bot.message_handler(content_types="text")
def send_translate(message):
        text1 = message.text.strip()
        url = "https://ftapi.pythonanywhere.com/translate"
    
        params = {
                "sl": "en",
                "dl": "ru",
                "text": text1
                }

        try:
                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()

                translated = response.json().get("destination-text", "Ошибка: перевода нет")
                bot.send_message(message.chat.id, translated)

        except requests.RequestException as e:
                bot.send_message(message.chat.id, f"Ошибка запроса: {e}")


                


print("Бот запущен.")


bot.polling(none_stop=True, interval=1)