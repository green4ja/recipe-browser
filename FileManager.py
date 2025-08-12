import json

class FileManager:
    def __init__(self):
        self.ALL_POSSIBLE_INGREDIENTS_FILE = "data/all_possible_ingredients.json"

    def return_all_possible_ingredients(self):
        try:
            with open(file=self.ALL_POSSIBLE_INGREDIENTS_FILE, mode='r', encoding='utf-8') as file:
                ingredients = json.load(file)
                return ingredients
        except Exception as e:
            print(f"Error loading ingredients file: {e}")
            return []
        
# if __name__ == "__main__":
#     f = FileManager()
#     print(f.return_all_possible_ingredients())