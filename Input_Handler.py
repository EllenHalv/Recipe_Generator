import os
from Functions import *

def input_ingredients():
    all_ingredients()
    ingredients_input = input("Enter ingredients separated by commas: ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    find_meals_with_ingredients(ingredients)

def press_enter():
    input("\n >> Press Enter to return to menu >>")
