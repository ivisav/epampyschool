import json
from datetime import datetime
import requests
import redis

api = 'YOUR API HERE'
city = 'Moscow'
# Host and port should be the same as you configured in your DB
rconnect = redis.Redis(host='localhost', port=6379, db=0)

raw_forcast = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},ru&appid={api}&units=metric")
# We should proceed with gathering of information only if got ok response from server
if raw_forcast.status_code == 200:
    weather = raw_forcast.json()
    main_condition = weather['weather'][0]['main']
    temp = weather['main']['temp']
    hum = weather['main']['humidity']
    now = datetime.now()
    timestamp = datetime.timestamp(now)     # date to timestamp
    prepared = json.dumps([main_condition, temp, hum, timestamp])
    rconnect.rpush(city, prepared)  # Data to Redis
else:
    print("Houston, we have a problem")
