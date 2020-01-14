import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import loads

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:Jl011187@cluster0-u6mnz.mongodb.net/cook_book?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/recipes_search')
def recipes_search():
    return render_template("search.html", 
    cuisines=mongo.db.cuisines.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", 
    cuisines=mongo.db.cuisines.find(),
    tools=mongo.db.tools.find())  

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/cuisine_match', methods=["POST"])
def cuisine_match():
    the_cuisine = request.form['cuisine_name']
    search_recipes = mongo.db.recipes.find({'cuisine': the_cuisine})
    return render_template("recipes.html", search_recipes=search_recipes)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe(): 
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))        

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find()
    all_tools = mongo.db.tools.find()
    return render_template('editrecipe.html', recipe=the_recipe, cuisines=all_cuisines, tools=all_tools)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'cuisine':request.form.get('cuisine'),
        'main_ingredient': request.form.get('main_ingredient'),
        'ing_one': request.form.get('ing_one'),
        'method': request.form.get('method'),
        'tool_name':request.form.get('tool')
    })
    return redirect(url_for('get_reecipes'))

@app.route('/delete_recipe/<recipe_id>')  
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/get_cuisines')  
def get_cuisines():
    return render_template('cuisines.html',
    cuisines=mongo.db.cuisines.find())
    
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html',
    cuisine=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))

@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    cuisines = mongo.db.cuisines
    cuisines.update( {'_id': ObjectId(cuisine_id)},
    {
        'name':request.form.get('name'),        
    })
    return redirect(url_for('get_cuisines'))

@app.route('/delete_cuisine/<cuisine_id>')  
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({'_id':ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))

@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisine_doc = {'name': request.form.get('cuisine_type')}
    mongo.db.cuisines.insert_one(cuisine_doc)
    return redirect(url_for('get_cuisines'))


@app.route('/add_cuisine')
def add_cuisine():
    return render_template('addcuisine.html')

@app.route('/get_tools')  
def get_tools():
    return render_template('tools.html',
    tools=mongo.db.tools.find())

@app.route('/edit_tool/<tool_id>')
def edit_tool(tool_id):
    return render_template('edittool.html',
    tool=mongo.db.tools.find_one({'_id': ObjectId(tool_id)}))

@app.route('/update_tool/<tool_id>', methods=['POST'])
def update_tool(tool_id):
    tools = mongo.db.tools
    tools.update( {'_id': ObjectId(tool_id)},
    {
        'tool_name':request.form.get('tool_name'),
        'tool_description':request.form.get('tool_description'),
        
    })
    return redirect(url_for('get_tools'))

@app.route('/delete_tool/<tool_id>')  
def delete_tool(tool_id):
    mongo.db.tools.remove({'_id':ObjectId(tool_id)})
    return redirect(url_for('get_tools'))

@app.route('/insert_tool', methods=['POST'])
def insert_tool():
    tools = mongo.db.tools
    tools.insert_one(request.form.to_dict())
    return redirect(url_for('get_tools'))


@app.route('/add_tool')
def add_tool():
    return render_template('addtool.html')

@app.route('/buy_tool')
def buy_tool():
    return render_template('buytool.html',
    tools=mongo.db.tools.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)