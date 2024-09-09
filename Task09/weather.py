import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_wearther():
    print(f'\n*** Get Current Weather Conditions ***\n')

    city = input(f'\nPlease Enter A City Name: ')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # print(request_url)
    weather_data = requests.get(request_url).json()
    #print(weather_data)
    # pprint(weather_data) # prints json file in prettier format that is easy to read

    print(f'Current Weather for: {weather_data["name"]}')
    print(f'The temp is: {weather_data["main"]["temp"]}')
    print(f'{weather_data["weather"][0]["description"]} and Feels Like {weather_data["main"]["temp"]}\n')

if __name__ == "__main__":
    get_current_wearther()