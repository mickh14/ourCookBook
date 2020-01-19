**OurCookBook**



**Business Goal** : To deliver an easy to use website that will allow users to create, edit and easily view cook recipes. The recipes should be displayed in a visually appealing and user-friendly way. The site should also promote Cookbook kitchen tool brand.

Vist [OurCook](https://out-cook-book.herokuapp.com/get_recipes)[Book](https://out-cook-book.herokuapp.com/get_recipes)

**Table of Contents**

1. UX

- User Stories
- Design
  - Framework
  - Database
  - Colour Scheme
  - Typography
  - Icon
- Wireframes

1. Scope

- Features
- Views
- CRUD
- Features Left to Implement

1. Technologies Used

- Languages
- Libraries
- Tools
- Hosting

1. Testing
2. Deployment
3. Credits

- Content
- Media
- Acknowledgements
- Disclaimer

### UX

This is the milestone project that I have created for the &quot;Data Centric Development&quot; module, which is part of &quot;Full Stack Web Development Course&quot; offered by Code Institute.

The application allows users to store and easily access cooking recipes. Recipes are stored, and can be retrieved, from a Mongo DB.

The OurCookBook website has a dynamic interactive front end that allow users to store and easily access cooking recipes. On the back end, the website will connect to a Mongo DB to support users adding and easily access recipes.

The website will also allow OurCookBook Kitchen Appliance/tools to be added and promotes the OurCookBook brand

My goal in design was to deliver an easy to navigate website allowing users to easily add, read or edit recipes.

#### User Stories:

1. As a user I can add a recipe
2. As a user I can search for a recipe by cuisine
3. As a user I can add a cuisine
4. As a user I can add a tool
5. As a user I can easily navigate around website
6. As the manager I can promote our brand of kitchen tool
7. As a user I can purchase a Kitchen tool
8. As a user I can edit a recipe
9. As a user I can edit a cuisine
10. As a manager I can edit a tool
11. As a user I can remove a recipe
12. As a user I can remove a cuisine
13. As a user I can remove a tool

#### Design:

**Framework:**

- [**Materialize 1.0.0**](https://materializecss.com/)

To get a modern and clean layout, I used Materialize as a framework.

- [**jQuery 3.4.0**](https://code.jquery.com/jquery/)

For Javascript, I mainly used Jquery

- [**Flask 1.0.2**](https://palletsprojects.com/p/flask/)

Flask is the micro web framework that runs the application

**Database:**

I used Mongo DB for the DB, the entity relation diagram can be seen [here](https://github.com/mickh14/ourCookBook/blob/master/documentation/Entity%20Relationship.xlsx)

The database is made up of the following collections.

**Recipes**

- id: <ObjectId()>
- recipe\_name 
- cuisine
- season
- prep\_time
- cook\_time
- total\_time
- main\_ingredient
- ingredients
- steps
- tools
-

**cuisines**

- id: <ObjectId()>
- name: 

**tools**

- id: <ObjectId()>
- tool\_name
- tool\_description
- tool\_cost
- tool\_model
- tool\_color
- tool\_warranty

**main\_ingredient**

- id
- name

**Colour Scheme and Typography:**

I have gone with a simple colour scheme. Most colours are transparent to allow the backgrounds add to the website.

Garamond was used for the font headings and navigation elements

**Icon**

[Materialize icons](https://materializecss.com/icons.html) has been used for this project.

#### Wireframes: Can be found [here](https://github.com/mickh14/ourCookBook/blob/master/documentation/OurCookBook%20Wireframes.pdf)

### Scope

#### Features

1. Website Opens to Search page that is good to look at and obvious navigation
2. Each page has easy navigation
3. Header has menu with links to the pages (toggle button on mobile)
4. Footer has social links
5. Pages
  1. Search
    1. Landing/Home Page
    2. Navbar on top
    3. Enter criteria for recipes to be displayed (Recipe page)
  2. Recipe
    1. Page displayed with list of recipes that match search
    2. Navbar on top
  3. Add Recipe
    1. Accessed via link on Navbar
    2. Recipe parameters can be entered
    3. Submit will send details entered to DB
    4. Submit or cancel will return user to search
  4. Edit Recipe
    1. Accessed via edit button on Recipe page
    2. Recipe parameters can be updated
    3. Submit will update details on DB
    4. Submit or cancel will return user to recipes page
  5. Cuisine
    1. Page displayed with list of cuisines retrieved from DB
    2. Navbar on top
  6. Add Cuisine
    1. Accessed via link on Navbar
    2. Cuisine name can be entered
    3. Submit will send details entered to DB
    4. Submit or cancel will return user to search
  7. Edit Cuisine
    1. Accessed via edit button on Cuisine page
    2. Recipe name can be updated
    3. Submit will update details on DB
    4. Submit or cancel will return user to recipes page
  8. Kitchen Tool
    1. Page displayed with list of kitchen tools retrieved from DB
    2. Navbar on top
  9. Add Tool
    1. Accessed via link on Navbar and on recipe
    2. Tool name can be entered
    3. Submit will send details entered to DB
    4. Submit or cancel will return user to search
  10. Edit Tool
    1. Accessed via edit button on Kitchen Tool page
    2. Tool name can be updated
    3. Submit will update details on DB
    4. Submit or cancel will return user to recipes page

1. A delete feature for each of the below required which will remove the item from DB. The delete feature will be trigger with a button on the relevant item
  1. Recipe
  2. Cuisine
  3. Kitchen Tool
2. Recipe page will display a list of recipes with collapsible area
  1. Each recipe main and main ingredient will be displayed
  2. When recipe is clicked on then more details of recipe will be displayed
3. Main Ingredient page will display a list retrieved from DB
4. Cuisine page will display a list retrieved from DB
5. Kitchen Tools page will display a list retrieved from DB
6. The materialize carousal shows all the OurCookBook brand Kitchen Appliance  available in the app by moving sideways.

#### Views

The below HTML pages will provide views for ease of use of the Cook Book website:

- BASE: A template for all other pages to use
- [Search](https://out-cook-book.herokuapp.com/recipes_search) – User can enter a cuisine and retrieve all recipes of that cuisine type from the DB
  - Landing page when website opens and can also be access via link in Navbar
- [Recipes](https://out-cook-book.herokuapp.com/get_recipes) – Displays all recipes that are retrieved from the DB
  - Displayed as a result of search
- [Cuisines](https://out-cook-book.herokuapp.com/get_cuisines) – Displays all cuisines that are retrieved from the DB
  - Access via link on navbar
- [Buytools](https://out-cook-book.herokuapp.com/buy_tool) – Displays all tools that are retrieved from the DB
  - Accessed via Buy button on recipe or Shop link on navbar
- [Addrecipe](https://out-cook-book.herokuapp.com/add_recipe) – Allows use to enter a new recipe details and send to DB
  - Accessed via link on navbar
- [Addcuisine](https://out-cook-book.herokuapp.com/add_cuisine) - Allows use to enter a new cuisine details and send to DB
  - Access via &quot;Add Cuisine&quot; button on cuisines page
- [Eidtrecipe](https://out-cook-book.herokuapp.com/edit_recipe/5e21eaacae463ebca8664ed0) – Allows a user to update and existing recipe
  - Access via &quot;edit&quot; button on recipes page
- [editcuisine](https://out-cook-book.herokuapp.com/edit_cuisine/5e175cb17efa136052fd4ca9)– Allows a user to update and existing cuisine
  - Access via &quot;edit&quot; button on cuisine page



**CRUD**

#### Recipes:

- **Create:** Create new recipe and add to the DB with the &quot;add\_recipe&quot; and &quot;insert\_recipe&quot; features
- **Read:** Display all recipes that are retrieved from the DB using recipe\_search feature
- **Update:** Edit a recipe and update the DB record with the edit\_recipe and update\_recipe features
- **Delete:** Remove a recipe from the DB with the delete recipe feature that is triggered with the &quot;Delete button on the recipes page

#### Cuisines:

- **Create:** Create new cuisines and add to the DB with the &quot;add\_cuisine&quot; and &quot;insert\_cuisine&quot; features
- **Read:** Display all recipes that are retrieved from the DB using get cuisines feature
- **Update:** Edit a recipe and update the DB record with the edit\_cuisine and update\_cuisines features
- **Delete:** Remove a recipe from the DB with the delete\_cuisine feature that is triggered with the &quot;Delete&quot; button on the cuisines page

#### Tools:

- **Create:** Create new kethcen tool and add to the DB with the &quot;add\_tool&quot; and &quot;insert\_tool&quot; features
- **Read:** Display all recipes that are retrieved from the DB using get\_tools feature
- **Update:** Edit a recipe and update the DB record with the edit\_tool and update\_tool features
- **Delete:** Remove a recipe from the DB with the delete recipe feature that is triggered with the &quot;Delete&quot; button on the tools page

### Technologies Used

#### Languages

- [**HTML**](https://html.spec.whatwg.org/multipage/) used as the markup language
- [**CSS**](https://www.w3.org/Style/CSS/) used as the base for cascading styles.
- [**JavaScript**](https://developer.mozilla.org/en-US/docs/Web/JavaScript) used mostly for DOM manipulation
- [**Python3**](https://www.python.org/) used to run the backend application

#### Libraries

- [**Google Fonts**](https://fonts.google.com/) provided the fonts used throughout the project
- [**Materialize**](https://materializecss.com/) v1.0.0 used as the CSS framework for the project
- [**jQuery**](https://jquery.com/) used as the primary JavaScript **functionality**.
- [**Flask**](https://flask.palletsprojects.com/en/1.1.x/) v1.0.2 is the micro web **framework** that runs the application
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/) v2.10.1 is the **default** templating language for flask and is used to display data from the python application in the frontend html pages
- [**PyMongo**](https://flask-pymongo.readthedocs.io/en/latest/) 2.3.0 was used to enable **the** python application to access the Mongo database

#### Tools

- [**GITPOD**](https://gitpod.io/workspaces/) **is the IDE I used to put the project together**
- [**MongoDB Atlas**](https://www.mongodb.com/cloud/atlas) is used to store my database in the &#39;cloud&#39;
- [**GitHub**](https://github.com/mickh14/ourCookBook/blob/master/documentation/Entity%20Relationship.xlsx)[ ](https://github.com/mickh14/ourCookBook/blob/master/documentation/Entity%20Relationship.xlsx)provides hosting for software development version control using Git
- [**Balsamiq**](https://balsamiq.com/) was used to create the wireframes when initially planning this project
- [**Am I Responsive**](http://ami.responsivedesign.is/) to create the images in this readme file

#### Hosting

- [**Heroku**](https://dashboard.heroku.com/apps/out-cook-book) is used to host the app

### Testing

**Functional Testing**

- I completed exploratory testing
- Friends and family completed user acceptance testing
- The following functional tests were complete
  - View Recipes
  - Add recipe
  - Edit recipe
  - Remove recipe
  - View Cuisines
  - Add Cuisine
  - Edit cuisine
  - Remove cuisine
  - Buy tool from recipe
  - Buy tool from shop
  - Recipe search

**Validation Services**

The following validation services were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate **HTML**.

Errors are detected for the Jinja in my HTML files. All other code was validated without error.

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate **CSS**.
- [JSHint](https://jshint.com/) was used to validate JavaScript.
- [PEP8 Online](http://pep8online.com/) was used to validate Python.

app.py file is completely PEP8 compliant!



### Deployment

#### Deployment To Heroku

In order the deploy my project to Heroku I have completed the following steps:

#### GitPod IDE

- Created a Procfile with the command echo web: python run.py \&gt; Procfile.
- Created a requirement.txt file so Heroku know what python modules it will need to run my application with the command sudo pip freeze --local \&gt; requirements.txt
- Then git add and git commit the new prerequisites from the requirements.txt file and Procfile, then &#39;git push&#39; the undertaking to GitHub.

#### Heroku

- After loging into heroku I created a new app, using the name out-cook-book and set the region to Europe.
- Select out-cook-book application
- In the settings tab I clicked reveal config vars and entered the required environment variables, which in this case were:

IP 0.0.0.0

PORT 5000

- Click on &quot;Deploy&quot;
  - For &quot;Deployment method&quot; and select GitHub.
- Confirm the linking of the heroku app to the correct GitHub repository.
- In the heroku dashboard, click &quot;Deploy&quot;.
- In the &quot;Manual Deployment&quot; section of this page, made sure the master branch is selected and then click &quot;Deploy Branch&quot;.
- The site is now successfully deployed.

### Credits

#### Content

The recipes for OutCookBook were sourced from [bbcgoodfood.com](https://www.bbcgoodfood.com/).

The text for some of the recipe categories was taken from Wikipedia.

#### Media

The images for the recipes have been sourced from their respective recipes at [bbcgoodfood.com](https://www.bbcgoodfood.com/).

The images for the logo image,Category images on the home page were taken from google free images.

#### Acknowledgements

**Tutorials**

- [https://stackoverflow.com](https://stackoverflow.com/)
- [https://www.youtube.com/](https://www.youtube.com/watch?v=vVx1737auSE)
- Special thanks to Guido Cecilio Garcia, my Code Institute mentor.

Disclaimer

- The content of this website is educational purposes only.