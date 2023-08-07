import requests
import os
import pprint

spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"]

#os.environ.get('SPOONACULAR_API_KEY') eller os.environ["SPOONACULAR_API_KEY"] 

url = "https://api.spoonacular.com/recipes/findByNutrients"

min_protein = 40

query_params = "apiKey=" + spoonacular_api_key + \
            "&minProtein=" + str(min_protein) 

query = url + "?" + query_params

spoonacular_response = requests.get(query)

pprint.pprint(spoonacular_response.json())

#---------------------------------------------------------
response_API = requests.get('https://www.askpython.com/')
print(response_API.status_code)

# api key located under "userhome/apikey-spoonacular"
api_key = ""

#def getAPIKey():
    # hämta nyckeln här