![screenshot](/images/Screenshot.png)

## Author information:
- Nevydaylo Dima
- FI-C 26

# Recipe App

## Overview

The Recipe App is a web application that allows users to search for recipes, view detailed information about each recipe, and save their favorite recipes. The app integrates with the Spoonacular API to fetch recipe data.

## Features

- **Search Recipes**: Users can search for recipes by entering a query.
- **View Recipe Details**: Detailed information about each recipe, including ingredients and instructions.
- **Favorite Recipes**: Users can save their favorite recipes for easy access later.

## Installation

### Prerequisites

- Python 3.6 or higher
- Flask
- Requests

### Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/Nevydaylo/recipeWeb.git
   cd recipeWeb
   
2. **Create a Virtual Environment**
   ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install Dependencies**
    ```sh
   pip install -r requirements.txt
   
4. **Setup API-Key** 
- Replace **'your_spoonacular_api_key'** with your actual Spoonacular API key in ***main.py***. 

## Run the Application
   `python main.py`

### Access the Application
- Open your web browser and navigate to http://127.0.0.1:5000/


## Usage
**Search for Recipes**

- Enter a query in the search bar and click "Search".
- View the list of search results with brief details.
- Click "View" to see detailed information about a recipe.

## View Recipe Details
- Detailed ingredients list. 
- Step-by-step cooking instructions.

## Favorite a Recipe
- Click the heart icon to save a recipe to your favorites.
- Access your favorite recipes by clicking "Favorites" in the navigation bar.

## Project Structure
- **main.py**: The main Flask application file.
- **templates/:** HTML templates for the application.
- **index.html:** The main page template.
- **view_recipe.html:** Template for viewing detailed recipe information.
- **favorites.html:** Template for viewing favorite recipes.
- **static/:** Static files such as CSS and JavaScript.

## API Integration
The app integrates with the Spoonacular API to fetch recipe data. Ensure you have a valid API key and set it in main.py.

- Search Recipes: Uses the complexSearch endpoint to fetch recipes based on a query.
- Recipe Details: Uses the information endpoint to fetch detailed information about a recipe.

# References
[Spoonacular API](https://spoonacular.com/food-api),

[Python Documentation](https://docs.python.org/3/),

[Flask Documentation](https://docs.python.org/3/),

[w3Schools](https://www.w3schools.com/python/),

[Stack Overflow](https://stackoverflow.com/questions/26587527/cite-a-paper-using-github-markdown-syntax)



