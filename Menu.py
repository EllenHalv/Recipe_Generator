# x value
x = 0
# imported for clearing code
import os
# imported functions from a second file
from Functions import *

# while loop of main menu
while True:
  print("\nHello! How would you like to use the meal-generator?")
  print("\n1. Randomize a meal")
  print("2. Get meals based on ingredient")
  print("3. Get vegetarian meals")
  print("4. View a list of all meals")
  print("5. Exit program")
  print("6. Get meal by ingredients")
  print("\n------------------------------")
  
  x = int(input(">> Enter your choice >> : "))
  # int input
  if x == 1:
    os.system('cls||clear')
    print("Your random meal is: ")
    print("--------------------")
    print_random_meal()
    # runs the called function
  elif x == 2:
    os.system('cls||clear')
    print("Here are examples of ingredients:")
    print("---------------------------------")
    print_with_ingredients()
    # runs the called function
  elif x == 3:
    os.system('cls||clear')
    print("Here are examples of vegetarian meals:")
    print("-------------------------------------")
    print_veg()
    # runs the called function
  elif x == 4:
    os.system('cls||clear')
    print("All meals:")
    print("----------")
    print_all_meals()
    # runs the called function
  elif x == 5:
    os.system('cls||clear')
    print("You have chosen to exit the program")
    input("\n >> Press Enter to exit >>")
    break
    # ends the program
  elif x == 6:
    os.system('cls||clear')
    print("Here are examples of ingredients:")
    print("---------------------------------")
    input_ingredients()
    # runs the called function
  else:
    os.system('cls||clear')
    print("Invalid choice. Please enter a number between 1-5")
    print("-------------------------------------------------")
    # error message if invalid choice is entered

print("Programmet har avslutats")