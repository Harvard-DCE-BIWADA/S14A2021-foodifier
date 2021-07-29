import os
import sys
import logging
from flask.helpers import total_seconds
from sqlalchemy.sql.expression import update
from dotenv import load_dotenv
from os import abort, environ, error
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session, send_from_directory, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, bindparam
from models.models import Db, users, foods
#from models.goals import UserGoals
from forms.forms import SignupForm, LoginForm, UpdateGoals
from passlib.hash import sha256_crypt
import gunicorn
import numpy as np
from werkzeug.utils import secure_filename
from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import tensorflow as tf
import requests
#import cv2
from urllib.parse import urlparse
import urllib.request 
import json
import uuid





# Load environment
load_dotenv('.env')


UPLOAD_FOLDER = 'static/uploads'

# Initialize app
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#app.run(debug=True, use_reloader=False)


# Initialize DB
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') # this is to solve a bug in heroku
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(environ.get('DATABASE_URL'))
Db.init_app(app)



global total_calories
total_calories = 0
@app.route('/')
def index():
    print(session)
    if 'username' in session:
        return render_template('index.html', logged_in = True)
    else:
        return render_template('index.html', logged_in = False)
    
     # home page --> give idea of app/introduces the product 

@app.route('/user/create',  methods=['POST'])
def user_create():
    
    # Init credentials from form request
    username = request.form['username']
    password = request.form['password']

    # Init user from Db query
    existing_user = users.query.filter_by(username=username).first()

    # Control new credentials
    if username == '' or existing_user:
        flash('The username already exists. Please pick another one.')
        print("error")
        return redirect(url_for('signup'))
    else:
        user = users(username=username, password=sha256_crypt.hash(password),weeklyg = 0, weekly = 0, dailyg = 1000, daily = 0)        
        Db.session.add(user)
        Db.session.commit()
        #user = User.query.filter_by(username=username).first()
        #print(user.uid)
        #user_goals = UserGoals(uid = user.uid, weeklyg = 0, weekly = 0, dailyg = 1000, daily = 0)
        #Db.session.add(user_goals)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))



    

    
    

@app.route('/login', methods=['GET', 'POST'])
def login():

    # Init form
    form = LoginForm()

    # If post
    if request.method == 'POST':

        # Init credentials from form request
        username = request.form['username']
        password = request.form['password']

        # Init user by Db query
        user = users.query.filter_by(username=username).first()
        print(user)

        # Control login validity
        if user is None or not sha256_crypt.verify(password, user.password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            session['username'] = username
            return redirect(url_for('profile'))

    # If GET
    else:
        return render_template('login.html', title='Login', form=form)



@app.route('/logout', methods=['POST'])
def logout():
    # Logout
    global total_calories
    total_calories = 0
    session.clear()
    return redirect(url_for('index'))
    


@app.route('/signup')
def signup():
    # Init form
    form = SignupForm()

    return render_template( 'signup.html', title='Signup', form=form )
"""
@app.route('/edit_goals')
def edit_goals():
    form = UpdateGoals()
    return render_template('form.html', form=form)
"""
@app.route('/profile')
def profile():
    app.logger.info("hello world")
    if 'username' in session: 
        if session['username'] != '':
            user = users.query.filter_by(username=session['username']).first()
            uid = user.uid
            dailyg = user.dailyg
            calories = user.daily
            print(uid)
            global total_calories
            user_goals = users.query.filter_by(uid=uid).first()
            return render_template('Dashboard.html', session_username = session['username'],calories=calories, daily_goal = dailyg) # where the user can set up their profile/calorie goals etc...
    else:
        return redirect("login")
"""
@app.route('/update/goals', methods = ['POST'])
def update_goals():
    user = User.query.filter_by(username=session['username']).first()
    uid = user.uid
    user_goals = UserGoals.query.filter_by(uid=uid).first()
    print(user_goals)
    user_goals.daily = request.form['goal']    
    Db.session.commit()
    return redirect(url_for('profile'))
"""
@app.route('/about')
def extra_info():
    if 'username' in session:
        return render_template("about.html", logged_in = True) # adds additional information about the food and health concepts + about how the model works and apis + resources
    else:
        return render_template("about.html", logged_in=False)


def save_uploaded_image( file ):
    if file and allowed_file( file.filename ):
        file_name = secure_filename( file.filename )
        file_path = os.path.join( app.root_path, app.config[ 'UPLOAD_FOLDER' ], file_name )
        file.save( file_path )
        return file_path
    else:
        flash( "Couldn't save uploaded image!", 'danger' )
        return False
        
def save_linked_image( link ):
    #print(link)
    if link and link != '':
        file_name = str( uuid.uuid4() ) + '.png'
        print( file_name )
        file_path = os.path.join( app.root_path, app.config[ 'UPLOAD_FOLDER' ], file_name )
        urllib.request.urlretrieve( link, file_path )
        return file_path
    else:
        flash( "Couldn't retrieve image!", 'danger' )
        return False

#ADAPTED FROM https://github.com/mitkir/keras-flask-image-classifier
@app.route('/submit_image', methods=['GET', 'POST'])
def upload_file():
    print("upload image", flush=True, file=sys.stdout
)
    if request.method == 'POST':

        if 'upload' in request.files:
            file = save_uploaded_image( request.files.get("upload") )
        elif( request.form[ 'link' ] ):
            file = save_linked_image( request.form['link'] )
        #abort
        # if not file:
        #     flash( "Couldn't process image!", 'warning' )
        #     return redirect( url_for( 'index' ) )
            
        print( "file to process: ", file, file.split( '/' )[ -1 ] )
        
        probs, output = predict( file )
        print( output )
        sorted( output, key = output.get )
        class_names = [ 'frozen_yogurt', 'hot_dog', 'pizza' ]

        print(
            "This image most likely belongs to {}"
            .format(class_names[np.argmax(probs)])
        )
        
        return render_template("submit.html", label = output, imagesource = file.split( '/' )[ -1 ], prediction = class_names[np.argmax(probs)]) # area where you can submit the image for recognition


    return render_template("submit.html")
@app.route('/calories/<foodname>', methods =['POST', 'GET'])
def calories(foodname):
    if request.method == 'GET':
        
        html_food_name = foodname.replace("_", " ")
        foodname = foodname.replace("_", "%20")
        print(html_food_name)
        
        info = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?app_id=c344f636&app_key=d2f4167ff9fc425ee9b8e5569d56e8f5&ingr={foodname}&nutrition-type=logging&category=generic-foods").json()
        try:
            calories = info["parsed"][0]["food"]["nutrients"]["ENERC_KCAL"]
        except:
            try:
                calories = info["hints"][0]["food"]["nutrients"]["ENERC_KCAL"]
            except:
                calories = "No Information Available"
        try:
            protein = info["parsed"][0]["food"]["nutrients"]["PROCNT"]
        except:
            try:
                protein = info["hints"][0]["food"]["nutrients"]["PROCNT"]
            except:
                protein = "No Information Available"
        try:
            fat = info["parsed"][0]["food"]["nutrients"]["FAT"]
        except:
            try:
                fat = info["hints"][0]["food"]["nutrients"]["FAT"]
            except:
                fat = "No Information Available"

        try:
            fibre = info["parsed"][0]["food"]["nutrients"]["FIBTG"]
        except:
            try:
                fibre = info["hints"][0]["food"]["nutrients"]["FIBTG"]
            except:
                fibre = "No Information Available"
    
        print(f"calories: {calories}\nprotein: {protein}\nfat: {fat}\nfibre: {fibre}")
        return render_template("calories.html", name=html_food_name, calories=calories, protein=protein, fat=fat, fibre=fibre)
        # shows the calories from the image (maybe not just calories)
    """
    else:
        username = session['username']
        user = users.query.filter_by(username=username).first()
        #add_calories(foodname)
        global total_calories
        total_calories += float(foodname)
        print (str(total_calories))
        user.daily = int(total_calories)
        user.weekly = int(total_calories)
       
        uid = user.uid
        calorie = int(total_calories)
        food = foods(uid = uid, foodname = 'test', calorie = total_calories)
        
        Db.session.add(food)
        Db.session.commit()
        return redirect(url_for('profile'))
    """

@app.route('/add_food', methods = ['POST'])
def add_food():
    user = users.query.filter_by(username=session['username']).first()
    food_name = request.form['foodname']
    calories = float(request.form['calories'])
    print(type(user.daily), type(user.weekly))

    user.daily += int(calories)
    user.weekly += int(calories)
    Db.session.commit()

    food = foods(uid = user.uid, foodname = food_name, calorie = calories)
    Db.session.add(food)
    Db.session.commit()
    return redirect(url_for('profile'))

@app.route('/daily_total')
def daily_total():
    return render_template("daily.html") # shows the daily dashboard/nutrition stats of a user for the day

@app.route('/weekly_total')
def weekly_total():
    return render_template("weekly.html") # shows the weekly dashboard/weekly total stats for the user

@app.route('/history')
def history():
    return render_template('index.html') # shows previous meals/calorie counts from either previous days or weeks


#ADAPTED FROM - https://github.com/mitkir/keras-flask-image-classifier/blob/master/application.py 

allowed_extensions = set(["jpg", "jpeg", "png"])
image_size = (600, 600)

model = load_model(environ.get('MODEL_PATH'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allowed_extensions

def predict(file):
    print("running predict")
    img = load_img(file, target_size = image_size)
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    probs = model.predict(img)[0]
    print(probs)
    print( model.predict_classes, flush=True)
    output = {'Frozen Yogurt' : probs[0], "Hot Dog" : probs[1], "Pizza" : probs[2]}
    #score = tf.nn.softmax(probs[0])
    return probs, output

@app.route('/corrected_food', methods = ['POST'])
def corrected_food():
    food = request.form['food']
    return redirect(f'/calories/{food}')

