# importing Flask from flask module
from flask import Flask,jsonify
# creating app using __name__
app = Flask(__name__)

items_list = ["soap", "shampoo", "tshirt", "shirt", "trousers", "misc"]
items = { items_list[x] : ((x+1)*100) for x in range(len(items_list))}

@app.route("/")
def static_hello():
    return "<h1>Welcome to my static page!</h1>"

@app.route("/users/<int:userid>")
def dynamic_userId(userid):
    return f"<h2>Welcome to dynamic page: {userid}"

@app.route("/items/<string:itemname>")
def dynamic_itemname(itemname):
    if itemname in items:
        return f"Price of {itemname} is: {items[itemname]}"
    else:
        return f"We do not have: {itemname}."

@app.route("/jsonify")
def jsonify_example():
    return jsonify(creator="Akash",items=items_list,validity="15 days")