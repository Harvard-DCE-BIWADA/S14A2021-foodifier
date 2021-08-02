CSCI S14A - Building Interactive Web Applications for Data Analysis

## Project Plan

**Meeting Times**: Saturday-Sunday, Wednesday, Monday 3:30 - 4:30p (1 hour)

**Zoom Link**: https://harvard.zoom.us/j/94705248192?pwd=UGk0Q1FkQjdjUVhncUpJSnFCK1ZWZz09

**Github Repo**: https://github.com/Harvard-DCE-BIWADA/S14A2021-foodifier

**Website Design Template**: https://www.webmd.com/diet/healthtool-food-calorie-counter

**Website Location**: https://foodifier.herokuapp.com/

### Team Members

Arda Eğrioğlu
Alden Ebert

## Project Basics

The purpose of this project is to classify the provided photo and display the calorie range of the food which is in the photo. It will be distributed as an app which can help you measure your calorie in take. It will be implemented in a website which can be easily accesed by everyone and has a simple UI.

General description of how the project will work

## Project Structure

/app/				- The folder containing the app.
/app/app.py			- The main app entry point
/app/templates		- Where the templates live.

/app/static			- Static files, etc.

/framework/			- The models that we are going to use

The main components of the app are:

1. **Base** - This module contains the skeleton that the entire framework rests on. It is responsible
for checking for compatibility, as well as loading and securing the various sub-modules.

2. **Tenserflow model** - The model we use to classify the foods.

3. **Food API** - The API we use to determine the calories of food.

## Project Timeline

Milestone 1: The creation of this document, and development of the project plan and basic structure.
Milestone 2: Doing the ground work for our Minimum Viable Product and catching up on milestone 1
Milestone 3: ???
Milestone 4: ???
Milestone 5: ???
Milestone 6: Present

## In The Future

1. There are many ways we could improve our app in the future. In the future we would implement a cleaner, more friendly looking U.I., try to improve the model, look into more apis (some of the calorie counts seem odd for the foods), implement tracking in more features other than just calories, and reccomend weekly and daily goals for the users based on what they want to achieve, their weight, and their height. We would also want to get this hosted online, but the model is too big for heroku and whenever we try to load it, the app crashes on heroku.  
