from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
from urllib.parse import unquote
import logging

app = Flask(__name__)
API_KEY = '940a54d866ef4924afd1ff202d719e25'
app.secret_key = 'supersecretkey'

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html', recipes=[], search_query='')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('search_query', '')
        recipes = search_recipes(query)
        return render_template('index.html', recipes=recipes, search_query=query)

    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)
    recipes = search_recipes(decoded_search_query)
    return render_template('index.html', recipes=recipes, search_query=decoded_search_query)

def search_recipes(query):
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return []

@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    search_query = request.args.get('search_query', '')
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipe = response.json()
        return render_template('view_recipe.html', recipe=recipe, search_query=search_query)
    return "Recipe not found", 404

@app.route('/add_to_favorites', methods=['POST'])
def add_to_favorites():
    recipe_id = request.form['recipe_id']
    if 'favorites' not in session:
        session['favorites'] = []
    if recipe_id not in session['favorites']:
        session['favorites'].append(recipe_id)
        session.modified = True
    logging.debug(f'Added recipe {recipe_id} to favorites. Current favorites: {session["favorites"]}')
    return jsonify({'status': 'success', 'message': 'Recipe added to favorites'})

@app.route('/favorites')
def favorites():
    favorite_recipes = []
    if 'favorites' in session:
        for recipe_id in session['favorites']:
            url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
            params = {'apiKey': API_KEY}
            response = requests.get(url, params=params)
            if response.status_code == 200:
                favorite_recipes.append(response.json())
    return render_template('favorites.html', recipes=favorite_recipes)

if __name__ == '__main__':
    app.run(debug=True)
