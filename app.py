# To access events, become facebook marketing partner https://developers.facebook.com/docs/graph-api/reference/event/

from flask import Flask, render_template
import json
import facebook
from datetime import datetime
from time import strptime, strftime

# Configure application
app = Flask(__name__)

# Get API
token = {"EAAFKVKHsjTsBAKqhUPo58NLBj8MrQfdnKaugMZAEMhuoM9wE9DQ4QCQGSYQdMciAHmjMZBwnc9SnRyuXY7giumXYEBSP3rivLZBabJcaO2TYQqtNqaYVojH86cCvhpscZBXjPB6TxvIT2t1c3gkZCl4euTNffU7Vuz8j3cWCmSpoSuwaDkFO5Ut19Xh592q2dVaiu8RkZCZAoHoQ2ZB4zxhdJOS1NRL5nCo9gNF6LJPnTlxx3037Ku0g"}
graph = facebook.GraphAPI(token, version=2.8)
events = graph.get_connections(id='me', connection_name='events')


print("events", events)
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