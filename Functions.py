import os
import random
from Input_Handler import *

# class for all dinners
class Dinner:
    def __init__(self, name, veg, ingredients):
        self.name = name
        self.veg = veg
        self.ingredients = ingredients
        
dinner = []
# List of all dinners
dinner.append(Dinner("Lasagne", "meat", ["pasta", "ground beef", "tomato", "onion", "cheese"]))
dinner.append(Dinner("Swedish Meatballs", "meat", ["ground beef", "lingonberry", "brunsås"]))
dinner.append(Dinner("Hamburger", "meat", ["ground beef", "tomato", "cheese", "sallad"]))
dinner.append(Dinner("Carbonara", "meat", ["pasta", "ground beef", "tomato"]))
dinner.append(Dinner("Pasta Sallad", "vegetarian", ["pasta", "sallad", "tomato"]))
dinner.append(Dinner("Gazpacho", "vegetarian", ["tomato"]))
dinner.append(Dinner("Pizza", "meat", ["cheese", "tomato", "ham"]))
dinner.append(Dinner("Broccoli pie", "meat", ["broccoli", "eggs", "cheese", "bacon"]))
dinner.append(Dinner("Carrot soup", "vegetarian", ["carrot", "ginger", "cream"]))
dinner.append(Dinner("Tacos", "meat", ["ground beef", "tortillas", "tomato", "avocado", "cheese"]))

# All functions

def all_ingredients():
    ingredients = []
    # list of all ingredients
    for food in dinner:
        for f in food.ingredients:
            if f not in ingredients:
                ingredients.append(f)
                # ingredients from "dinner list" are imported to "ingredients list"
    print(ingredients)

def print_all_meals():
    for meal in dinner:
        print(meal.name)
        # names of all meals are printed
    press_enter()
    os.system('cls||clear')

def print_random_meal():
    meal_names = []
    # list of all meal names
    for meal in dinner:
        meal_names.append(meal.name)
        # names from "dinner list" are imported to "meal_names list"
    print("\n" + random.choice(meal_names))
    # a random meal name is printed
    press_enter()
    os.system('cls||clear')

def print_veg():
    for meal in dinner:
        if meal.veg == "vegetarian":
            print("\n" + meal.name)
            # if a meal from "dinner list" is vegetarian it is printed
    press_enter()
    os.system('cls||clear')

def print_meat():
    for meal in dinner:
        if meal.veg == "meat":
            print("\n" + meal.name)
            # if a meal from "dinner list" has meat it is printed
    press_enter()
    os.system('cls||clear')

def find_meals_with_ingredients(ingredients):
    matching_meals = []  # Lista för matchande måltider

    for meal in dinner:
        if set(ingredients).issubset(set(meal.ingredients)):
            matching_meals.append(meal)

    print("\nMeals that use all the ingredients:", ingredients)
    print("-------------------------------------------------")
    for meal in matching_meals:
        print(meal.name)

