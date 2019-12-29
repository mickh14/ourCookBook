import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:Jl011187@cluster0-u6mnz.mongodb.net/cook_book?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

@app.route('/recipe')
def add_recipe():
    return render_template("addrecipe.html", 
    categories=mongo.db.categories.find())   

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))        

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'cuisine':request.form.get('cuisine'),
        'main_ingredient': request.form.get('main_ingredient'),
        'other_ingredient': request.form.get('other_ingredient'),
        'method': request.form.get('method'),
        'tool':request.form.get('tool')
    })
    return redirect(url_for('get_reecipes'))

@app.route('/delete_recipe/<recipe_id>')  
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/get_cuisines')  
def get_cuisines():
    return render_template('cuisines.html',
    cuisines=mongo.db.cuisine.find())
    
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html',
    cuisine=mongo.db.cuisine.find_one({'_id': ObjectId(cuisine_id)}))

@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.categories.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_type': request.form.get('cuisine_type')})
    return redirect(url_for('get_cuisines'))

@app.route('/delete_cuisine/<cuisine_id>')  
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove({'_id':ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))

@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    category_doc = {'cuisine_type': request.form.get('cuisine_type')}
    mongo.db.categories.insert_one(cuisine_doc)
    return redirect(url_for('get_cuisines'))


@app.route('/add_cuisine')
def add_cuisine():
    return render_template('addcuisine.html') 


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)