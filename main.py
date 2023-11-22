import requests

API_KEY = "9928499d600b9a7c1092e737b8faad18"

URL = "https://api.openweathermap.org/data/2.5/weather"


def get_city():
    return input("Введите название города!:\n")


def request(city, appid=API_KEY, lang="ru", url=URL):
    params = {
        "q": city,
        "appid": appid,
        "lang": lang

    }
    response = requests.get(url, params)
    if response.status_code == 200:
        return response.json()


def main():
    print('Привет')
    while True:
        city = get_city()
        response = request(city)
        if response:
            break
        print("Не смог найти этот населённый пункт :D, повторите попытку")
    data = get_data(response)
    msg = message(data, city)
    print(msg)


def get_data(response):
    data = dict()
    data['description'] = response['weather'][0]['description']
    data['temp'] = int(response['main']['temp'] - 265.03)
    data['feels'] = int(response['main']['feels_like'] - 258.86)
    data['wind'] = response['wind']['speed']
    data['pressure'] = response['main']['pressure']
    return data


def message(data, city):
    return (f"погода в {city.capitalize()}:\n"
            f"{data['description'].capitalize()}\n"
            f"температура: {data['temp']}C, "
            f"ощущается как: {data['feels']}C\n"
            f"скорость ветра: {data['wind']}м/c\n"
            f"давление: {data['pressure']} мм р.с.")


main()
