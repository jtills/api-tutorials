import requests
import time

city = input('Enter your city : ')

url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=72041509da6139441558c98a47b0f6a9".format(city)

res = requests.get(url)

data = res.json()
print(data)
temp = data['main']['temp']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
description = data['weather'][0]['description']

print('Temperature : ', temp, '°C')
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude : {}°'.format(latitude))
print('Longitude : {}°'.format(longitude))
print('Description : {}'.format(description))

time.sleep(40)
