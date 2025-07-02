# app_lab.py
# Task 2 : Hello World
# Task 3 : Add Templates
# Author: Andre Gutierrez
# Date: 7/2/25
# CST 205
# A Flask app that displays favorite acronyms

from flask import Flask, render_template

# Creates the Flask application object
unique_app = Flask(__name__)

# List of favorite acronyms and names (Names and acronyms chosen by me)
favorite_acronyms = [
    {"name": "Andre", "acronym": "LMAO", "reason": "Because it's funny!"},
    {"name": "Emma", "acronym": "OMW", "reason": "I use it all the time."},
    {"name": "Emiliano", "acronym": "IDK", "reason": "It's useful."}
]

@unique_app.route('/')
def show_acronyms():
    # Builds the HTML content with acronyms
    html_content = "<h1>Favorite Acronyms</h1>"
    for entry in favorite_acronyms:
        html_content += f"<p>{entry['name']}: {entry['acronym']} - {entry['reason']}</p>"
    return html_content

@unique_app.route('/hello')
def hello_world():
    return "Hello World"

# Task 3 : Route using a template and variables
@unique_app.route('/andre')
def show_my_acronym():
    return render_template(
        'template_lab.html',
        user_name="Andre",   
        user_acronym="LOL",               
        user_reason="Because it's funny!"
    )

# Runs the app only if this file is executed directly
if __name__ == '__main__':
    unique_app.run(debug=True)


