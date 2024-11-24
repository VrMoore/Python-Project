import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Indonesia?unitGroup=metric&key={api_key}&contentType=json")

if response.status_code == 200 :

    data = response.json()
    location = data['resolvedAddress']
    desc = data['description']
    day = data['days']

    for i in range(7) : 
        datetime = day[i]['datetime']
        temperature_max = day[i]['tempmax']
        temperature_min = day[i]['tempmin']
        humid = day[i]['humidity']
        conds = day[i]['conditions']
        decs_of_day = day[i]['description']

        print(f'Location :  {location} , Date : {datetime}')
        print(f'{desc}')
        print(f'Tempereture : {temperature_min} ~ {temperature_max} \t Humidity : {humid}')
        print(f'{conds}\n{decs_of_day}')