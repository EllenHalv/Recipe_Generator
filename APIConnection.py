import requests

response_API = requests.get('https://www.askpython.com/')
print(response_API.status_code)