# -*- coding: utf-8 -*-

import requests
from datetime import datetime, timedelta

API_KEY = 'c372a60acf44c62ed5ce4f4b28bacca5'
CITY = 'Jakarta'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)
data = response.json()

forecast = data['list']
daily_temps = {}

for entry in forecast:
    date_time = datetime.fromtimestamp(entry['dt'])
    if date_time.hour == 12:  # Filter for 12:00 PM
        date = date_time.date()
        temp = entry['main']['temp']
        daily_temps[date] = temp

print("Weather Forecast:")
for date, temp in daily_temps.items():
    formatted_date = date.strftime('%a, %d %b %Y')
    print(f"{formatted_date}: {temp:.2f}°C")
