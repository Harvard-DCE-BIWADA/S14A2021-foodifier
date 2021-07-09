from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


# Initialize app
app = Flask(__name__)

@app.route('/')
def index():
    #users = HomeworkUser.query.all()
    #print('# users:', len(users))
    return render_template("index.html")

@app.route('/submit_image')
def submit_image():
	return render_template("submit.html")

@app.route('/calories')
def calories():
	return render_template("calories.html") #shows the calories from the image

@app.route('/daily_total')
def daily_total():
    return render_template("daily.html")

@app.route('/weekly_total')
def weekly_total():
    return render_template("weekly.html")
    