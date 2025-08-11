import requests


class API:
    """
    Handles any interactions with theMealDB API.
    """

    def __init__(self):
        """
        Initializes class variables.
        """
        self.api_base_url = "https://www.themealdb.com/api/json/v1/1/"

    def get_random_recipe(self):
        """
        Fetches a random recipe from theMealDB API and returns the data dictionary.
        """
        api_random_recipe_url = f"{self.api_base_url}random.php"
        try:
            api_response = requests.get(
                url=api_random_recipe_url, timeout=10
            )  # 10-second timeout protection
            api_response.raise_for_status()
            api_response_json = api_response.json()
        except requests.exceptions.RequestException as e:
            api_response_json = {}
            print(e)
        return api_response_json


# if __name__ == "__main__":
#     a = API()
#     a.get_random_recipe()
