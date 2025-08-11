import requests
import json

"""
Used for writing all possible ingredients to the all_possible_ingredients.json
"""

r = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
r_json = r.json()
li = [item.get('strIngredient') for item in r_json['meals']]

try:
    with open(file='data/all_possible_ingredients.json', mode='w', encoding='utf-8') as file:
        json.dump(li, file, indent=4)
except Exception as e:
    print(e)