import os
from dotenv import load_dotenv
from os import environ, error
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from models.models import Db, User, Post
from forms.forms import SignupForm, LoginForm
from passlib.hash import sha256_crypt
import gunicorn
import numpy as np
from werkzeug.utils import secure_filename
from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import tensorflow as tf
import requests

# Load environment
load_dotenv('.env')

UPLOAD_FOLDER = 'uploads'

# Initialize app
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize DB
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') # this is to solve a bug in heroku
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(environ.get('DATABASE_URL'))
Db.init_app(app)




@app.route('/')
def index():
    print(session)
    return render_template('index.html')
    
     # home page --> give idea of app/introduces the product 

@app.route('/user/create',  methods=['POST'])
def user_create():
    
    # Init credentials from form request
    username = request.form['username']
    password = request.form['password']

    # Init user from Db query
    existing_user = User.query.filter_by(username=username).first()

    # Control new credentials
    if username == '' or existing_user:
        flash('The username already exists. Please pick another one.')
        print("error")
        return redirect(url_for('signup'))
    else:
        user = User(username=username, password=sha256_crypt.hash(password))
        Db.session.add(user)
        Db.session.commit()
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
        user = User.query.filter_by(username=username).first()
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
    session.clear()
    return redirect(url_for('index'))
    


@app.route('/signup')
def signup():
    # Init form
    form = SignupForm()

    return render_template( 'signup.html', title='Signup', form=form )
    


@app.route('/profile')
def profile():
    return render_template('Dashboard.html', session_username = session['username']) # where the user can set up their profile/calorie goals etc...

@app.route('/about')
def extra_info():
    return render_template("about.html") # adds additional information about the food and health concepts + about how the model works and apis + resources

#ADAPTED FROM https://github.com/mitkir/keras-flask-image-classifier
@app.route('/submit_image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            probs, output = predict(file_path)
            print(output)
            class_names = ['frozen_yogurt', 'hot_dog', 'pizza']

            print(
                "This image most likely belongs to {}"
                .format(class_names[np.argmax(probs)])
            )
    #return render_template("home.html", label=output, imagesource=file_path)
        print(file_path)
        return render_template("submit.html", label = output, imagesource = file_path, prediction = class_names[np.argmax(probs)]) # area where you can submit the image for recognition 
    return render_template("submit.html")
@app.route('/calories/<foodname>')
def calories(foodname):
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
    return render_template("calories.html", name=html_food_name, calories=calories, protein=protein, fat=fat, fibre=fibre) # shows the calories from the image (maybe not just calories)
    

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

model = load_model('/mnt/c/Users/simon/Desktop/food-101-demo-model')  

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allowed_extensions

def predict(file):
    img = load_img(file, target_size = image_size)
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    probs = model.predict(img)[0]
    print(probs)
    output = {'Frozen Yogurt' : probs[0], "Hot Dog" : probs[1], "Pizza" : probs[2]}
    #score = tf.nn.softmax(probs[0])
    return probs, output

