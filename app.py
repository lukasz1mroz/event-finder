# Extend the token instruction
# https://medium.com/@DrGabrielA81/python-how-making-facebook-api-calls-using-facebook-sdk-ea18bec973c8

from flask import Flask, render_template
import json
import facebook
from datetime import datetime
from time import strptime, strftime

# Configure application
app = Flask(__name__)

# Get API
token = {"EAAFKVKHsjTsBAIVr6XlWAgMZCbwG8oCa5b1MeZAcEqUGPfEwZATHA3V0IpwiYPEi71VTGgy2TtzKnSDiliVbZADR6DjJBEqdKupUnMlZA25BghDUgPd3ZAGncSNS6bnWkqePzdYDgiAzZBqF5HgZARA9zmcBxeJLZAJQ1rgvAB22L2AZDZD"}
graph = facebook.GraphAPI(token)
events = graph.get_connections(id="me", connection_name="events", fields="id, name, place, start_time, cover")

# Format date  
now = datetime.now()
formatted_now = now.strftime('%Y-%m-%dT%H:%M:%S+0200')

# Generate pages  for chosen options
@app.route("/")
def home():  
    return render_template("index.html", events=events, formatted_now=formatted_now)

@app.route("/nature")
def nature():
    return render_template("nature.html", events=events, formatted_now=formatted_now)

@app.route("/party")
def party():
    return render_template("party.html", events=events, formatted_now=formatted_now)

@app.route("/food")
def food():
    return render_template("food.html", events=events, formatted_now=formatted_now)

@app.route("/culture")
def culture():
    return render_template("culture.html", events=events, formatted_now=formatted_now)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()