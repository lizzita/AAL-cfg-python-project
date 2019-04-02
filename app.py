#from flask import Flask

#app = Flask(__name__)

#@app.route("/") #decorator
#def say_hello():
#  return "hello world!"

#app.run(debug=True) #automatic restart itself GREAT FOR WEB DEVELOPMENT
import os #access environment variables set by Heroku, which includes the port it has assigned to run your application on.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route("/<name>")
def say_hello_to1(name):
    return f"Coming soon! {name}"

@app.route("/<name>")
def say_hello_to(name):
  return render_template("index.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values

  return render_template("feedback.html", form_data=data)

#The following piece of conditional logic checks whether you are running your application on Heroku (in which case, the PORT environment variable would exist), or if you are running your application locally. The host=0.0.0.0 bit instructs your Flask application to listen on all web address. This is important to ensure the application runs on Heroku since we don't know which host Heroku will decide to host the application on.

if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)