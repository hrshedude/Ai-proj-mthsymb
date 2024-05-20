from flask import Flask, render_template, request

import synthlibhtml as slib

app = Flask(__name__)

button_text = "Click me!"

@app.route("/", methods=["GET", "POST"])
def index():
  global button_text
  if request.method == "POST":
    button_text = "Button Pressed!"
  return render_template("index.html", button_text=button_text)

if __name__ == "__main__":
  app.run(debug=True)
