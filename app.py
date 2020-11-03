from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
  return "<h1>Welcome to the world of Flask</h1>"

@app.route('/<showcase>')
def showCase(showcase):
  return "why u con dey "+showcase+" yourself."

@app.route('/show_todo')
def homePage():
  return render_template("home.html")

@app.route('/getmsg', methods=['GET'])
def getMessage():
  # Get name from URL parameter. e.g. /getmsg?key=value
  username = request.args.get("name", None)
  # For debugging
  print(f"got name n it is {username}")
  response = {}
  if not username:
    response["Error"] = "no name found. Please enter a name"
  elif str(username).isdigit():
    response["Error"] = "Username must be a string"
  else:
    response["message"] = f"Welcome {username} to our awesome platform!!"
  # Return response in json format
  return jsonify(response)

if __name__ == "__main__":
  app.run(debug=True, port=4003, threaded=True)
