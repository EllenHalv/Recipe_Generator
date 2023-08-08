# x value
x = 0
# imported for clearing code
import os
# imported functions from a second file
from Functions import *
from Input_Handler import *

# while loop of main menu
while True:
  print("\nHello! How would you like to use the recipe-generator?")
  print("\n1. Randomize a recipe")
  print("2. Get recipe based on ingredient")
  print("3. Get vegetarian recipies")
  print("4. View my saved recipies")
  print("5. Exit program")
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
    input_ingredients()
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
  else:
    os.system('cls||clear')
    print("Invalid choice. Please enter a number between 1-5")
    print("-------------------------------------------------")
    # error message if invalid choice is entered

print("Programmet har avslutats")