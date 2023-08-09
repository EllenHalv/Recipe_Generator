
def input_ingredients():
    ingredients_input = input("Enter ingredients separated by commas: ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    return ingredients

def press_enter():
    input("\n >> Press Enter to return to menu >>")
