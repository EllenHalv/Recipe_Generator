# Meal Generator

## Overview

The Recipe Generator is a Python application that interacts with the Spoonacular API to provide recipe suggestions based on user input for ingredients. It also includes functionality to fetch random recipes and detailed information about a specific recipe.

## Prerequisites

- Python 3.x
- Spoonacular API key (sign up [here](https://spoonacular.com/food-api))

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/EllenHalv/Recipe_Generator.git
    cd Recipe_Generator
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Spoonacular API key:

    - Get your API key from [Spoonacular](https://spoonacular.com/food-api).
    - Set the API key as an environment variable:

      ```bash
      export SPOONACULAR_API_KEY=your-api-key
      ```

      Alternatively, you can set the environment variable in your preferred way or manually.

4. Run the script:

    ```bash
    python main.py
    ```

## Usage

![Example]("Screenshot 2024-01-24 022048.png")

### 1. Find Recipes by Ingredients

The menu allows you to navigate easily and find recipes based on the ingredients you have. Enter a comma-separated list of ingredients when prompted. Or randomize recipes!

```bash
python main.py
