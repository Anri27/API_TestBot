 #АПИ С СОБАЧАМИ
@bot.message_handler(commands=["dog"]) 
def send_random_dog_image(message):
        try: 
                response = requests.get("https://dog.ceo/api/breeds/image/random", timeout=5)
                dog_image_url = response.json().get("message")
                bot.send_photo(chat_id=message.chat.id, photo=dog_image_url)
        except requests.RequestException:
                bot.reply_to(message, "ошибочка")





#АПИ С ПОГОДОЙ
WEATHER_TOKEN = "6303bc3cbf8954ea092271a924748948"


@bot.message_handler(commands=["start"])
def command_start(message):
    bot.reply_to(message, "Напиши название любого города.")



@bot.message_handler(content_types="text")
def send_weather(message):
        city = message.text.strip()
        url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&lang=ru&appid={WEATHER_TOKEN}&q={city}"
        
        
        try: 
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()
                print({response.status_code})
                
                
                weather = data["weather"][0]["description"].capitalize()
                temp = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                town = data["name"]
                country_name = data["sys"]["country"]
                coord_lon = data["coord"]["lon"]
                coord_lat = data["coord"]["lat"]


                reply = (
                f"🌍 Город: {town}\n"
                f"Страна: {country_name}\n"
                f"Долгота: {coord_lon}\n"
                f"Широта: {coord_lat}\n"
                f"☁️ Погода: {weather}\n"
                f"🌡️ Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"💧 Влажность: {humidity}%"
                )


                bot.send_message(message.chat.id, reply)
                print(f"Обработана команда /weather")


        except requests.RequestException:
                bot.reply_to(message, "ошибочка")