from config import open_weather_auth_token
from pprint import pprint
import requests
import datetime

def get_weather(city, open_weather_auth_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Сухо \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"

    }


    try:
        request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_auth_token}&units=metric"
        )
        response = request.json()
        pprint(response)

        get_weather_description = response['weather'][0]['main']
        if get_weather_description in code_to_smile:
            wd = code_to_smile[get_weather_description]
        else:
            wd = "Посмотри в окно дружище, не пойму что там происходит"

        get_city_name = response['name']
        get_temp = response['main']['temp']
        get_temp_max = response['main']['temp_max']
        get_temp_min = response['main']['temp_min']
        get_humidity = response['main']['humidity']
        get_pressure = response['main']['pressure']
        get_wind_speed = response['wind']['speed']
        get_sunrise_time = datetime.datetime.fromtimestamp(response['sys']['sunrise'])
        get_sunset_time = datetime.datetime.fromtimestamp(response['sys']['sunset'])
        get_length_of_the_day = datetime.datetime.fromtimestamp(response['sys']['sunset'])\
                                - datetime.datetime.fromtimestamp(response['sys']['sunrise'])
        get_data = datetime.datetime.now().strftime('%y-%m-%d-%H:%M:%S')
        print(
              f"***{get_data}***\n"
              f"Погода в городе: {get_city_name}\nТемпература: {get_temp} C°"
              f"\nМинимальная температура: {get_temp_min} C° {wd}\n"
              f"Максимальная температура: {get_temp_max} C°\nВлажность: {get_humidity}%"
              f"\nДавление: {get_pressure} мм.рт.мт\n"
              f"Скорость ветра: {get_wind_speed} м/с\nВремя восхода: {get_sunrise_time}\n"
              f"Время заказа: {get_sunset_time}\nПродолжительность светового дня: {get_length_of_the_day}"
              f"\nХорошего дня!"
        )
    except Exception as ex:
        print(ex)



def main():
    city = input("Введите название города - ")
    get_weather(city, open_weather_auth_token)


if __name__ == "__main__":
    main()