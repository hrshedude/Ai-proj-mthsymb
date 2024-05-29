from flask import Flask, render_template, request

import synthlibhtml as slib


itg = slib.items_stuff()







app = Flask(__name__)

sym_text = "Click me!"

@app.route("/", methods=["GET", "POST"])
def index():
  
  global sym_text
  
  if request.method == "POST":
    item = itg.getitem()
    if item != False:
      sym_text = str(item)
    else:
      sym_text = "Over"

  return render_template("index.html", sym_text=sym_text, save_name="nigga.png")

if __name__ == "__main__":
  app.run(debug=True)
