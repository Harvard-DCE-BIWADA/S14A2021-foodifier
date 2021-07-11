from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


# Initialize app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") # home page --> give idea of app/introduces the product 

@app.route('/create_account')
def create_account():
    return render_template("index.html") # page to create an account to save weekly/dail data + previous meals (maybe give suggestions) (index.html is a placeholder template)

@app.route('/login')
def login():
    return render_template("index.html") # page to login to your account so you can access previous data

@app.route('/profile')
def profile():
    return render_template('index.html') # where the user can set up their profile/calorie goals etc...

@app.route('/info')
def extra_info():
    return render_template("index.html") # adds additional information about the food and health concepts + about how the model works and apis + resources

@app.route('/submit_image')
def submit_image():
	return render_template("submit.html") # area where you can submit the image for recognition 

@app.route('/calories')
def calories():
	return render_template("calories.html") # shows the calories from the image (maybe not just calories)

@app.route('/daily_total')
def daily_total():
    return render_template("daily.html") # shows the daily dashboard/nutrition stats of a user for the day

@app.route('/weekly_total')
def weekly_total():
    return render_template("weekly.html") # shows the weekly dashboard/weekly total stats for the user

@app.route('/history')
def history():
    return render_template('index.html') # shows previous meals/calorie counts from either previous days or weeks


    