import datetime
import requests as requests
import os


GENDER = 'female'
WEIGHT_KG = 65
HEIGHT_CM = 166
AGE = 32


APP_ID = os.environ.get('APPID')
API_KEY = os.environ.get('API_KEYWORKOUT')

password_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': "application/json",
}
param = {
    "query": input('What exersice you have done?:'),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

responce = requests.post(url=password_endpoint, headers=headers, json=param)
data = responce.json()


sheety_endpoint = os.environ.get('SHEETENDPOINT')
day = datetime.datetime.now().strftime('%d/%m/%Y')
current_time = datetime.datetime.now().strftime("%H:%M:%S")

sheery_param = {
    'workout': {
        'date': day,
        'time': current_time,
    }
}

for el in data['exercises']:
    sheery_param['workout']['exercise'] = el['name'].title()
    sheery_param['workout']['duration'] = el['met']
    sheery_param['workout']['calories'] = el['nf_calories']
    sheety_responce = requests.post(url=sheety_endpoint, json=sheery_param, headers=headers,
                                    auth=(os.environ.get('AUTHWORKOUTNAME'), os.environ.get('AUTHWORKOUTPAS')
    ))


