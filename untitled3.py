# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PZ8GP_6plLAt5P9OflM4Wq5JKfDukHMC
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_list():
    result = []
    for i in range(100, 0, -1):
        if is_prime(i):
            continue
        if i % 3 == 0 and i % 5 == 0:
            result.append("FooBar")
        elif i % 3 == 0:
            result.append("Foo")
        elif i % 5 == 0:
            result.append("Bar")
        else:
            result.append(str(i))
    return result

result_list = generate_list()
print(result_list)

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