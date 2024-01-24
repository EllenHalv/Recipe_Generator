import os
import requests
import pprint
from Functions import *

# The key is in the system environment variables 
spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"] 


# Finds meals by input minumum grams of protein
def get_meal_by_protein():
    url = "https://api.spoonacular.com/recipes/findByNutrients"

    min_protein = 40

    query_params = "apiKey=" + spoonacular_api_key + \
                "&minProtein=" + str(min_protein) 

    query = url + "?" + query_params

    spoonacular_response = requests.get(query)

    pprint.pprint(spoonacular_response.json())


# Print response code debug
#---------------------------------------------------------
response_API = requests.get('https://www.askpython.com/')
print(response_API.status_code)
#---------------------------------------------------------

def include_ingredients():
    ingredients = input_ingredients()

    # Construct the Spoonacular API URL
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    query_params = {
        "ingredients": ",".join(ingredients),
        "number": 10  # You can adjust the number of recipes you want to retrieve
    }

    # Add your API key to the query parameters
    query_params["apiKey"] = spoonacular_api_key

    # Make the API request
    spoonacular_response = requests.get(url, params=query_params)

    if spoonacular_response.status_code == 200:
        recipes = spoonacular_response.json()
        print("Recipes:")
        for recipe in recipes:
            print(f"- {recipe['title']}")
    else:
        print(f"Error: {spoonacular_response.status_code}. Unable to retrieve recipes.")

def exclude_ingredients():
    ingredients = input_ingredients()
    url = "https://api.spoonacular.com/recipes/excludeIngredients"

# prints one random meal (title and ingredients)
def get_random_meal():
    url = "https://api.spoonacular.com/recipes/random"
    #random?number=1

    query_params = "apiKey=" + spoonacular_api_key

    query = url + "?" + query_params

    spoonacular_response = requests.get(query)

    if spoonacular_response.status_code == 200:
        json_data = spoonacular_response.json()

        filtered_data = []

        for recipe in json_data["recipes"]:
            title = recipe["title"]
            ingredients = []

            for ingredient in recipe["extendedIngredients"]:
                ingredient_name = ingredient["name"]
                ingredients.append(ingredient_name)

            # Create a dictionary to store the recipe information
            recipe_info = {
                "title": title,
                "ingredients": ingredients
            }

            # Print the recipe information in a structured format
            print(f"Title: {recipe_info['title']}")
            print(f"Ingredients: {recipe_info['ingredients']}")

            filtered_data.append(recipe_info)

            # TODO ask if user want to see the entire recipe


