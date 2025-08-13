import requests
import json
from API import API
from FileManager import FileManager

"""
Used for testing functionality.
"""

# a = API()
# meal = a.get_random_recipe()['meals'][0]
# # r = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
# # r_json = r.json()
# # meal = r_json['meals'][0]
# # ingredient_name_list = [
# #     value.lower()
# #     for key, value in meal.items()
# #     if key.startswith('strIngredient') and value and value.strip()
# # ]

# # ingredient_measure_list = [
# #     value.lower()
# #     for key, value in meal.items()
# #     if key.startswith('strMeasure') and value and value.strip()
# # ]

# recipe_data = {
#     "name": meal['strMeal'],
#     "instructions": meal['strInstructions'],
#     "youtubeVideoURL": meal['strYoutube'],
# }

# ingredients = []
# for i in range(1, 21):
#     ingredient = meal.get(f"strIngredient{i}")
#     measure = meal.get(f"strMeasure{i}")
#     if ingredient and ingredient.strip():
#         ingredients.append({
#             "name": ingredient.lower(),
#             "measure": measure.strip() if measure else ""
#         })
#         print(f"i = {i}")
#     else:
#         break # exit loop on first empty ingredient

# recipe_data["ingredients"] = ingredients

# print(meal)
# print(recipe_data)
# # print(ingredient_name_list)
# # print(ingredient_measure_list)

# # Load recipes
# try:
#     with open(file="data/complete_recipes.json", mode="r", encoding="utf-8") as file1:
#         recipes = json.load(file1)
# except Exception as e:
#     recipes = []
#     print(e)

# recipes.append(recipe_data)

# # Add new recipe
# try:
#     with open(file="data/complete_recipes.json", mode="w", encoding="utf-8") as file2:
#         json.dump(recipes, file2, indent=4)
# except Exception as e:
#     print(e)

f = FileManager()
recipes = f.return_all_complete_recipes()
for recipe in recipes:
    name = recipe.get("name")
    print(name)