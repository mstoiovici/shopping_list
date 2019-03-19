from flask import Flask, render_template,redirect, request, jsonify
import sqlite3
from engine import *

app = Flask(__name__)

# Home page
@app.route('/')
def index():

    return render_template('index.html')
"""
@app.route("/item_list",methods=["GET"])
def get_item_list():
    items=get_information()
    return render_template('item_list.html', **locals())
"""

@app.route("/item_new",methods=["GET", "POST"])
def get_item_new():
    form_data = request.form
    title=form_data["title"]
    description=form_data["description"]
    new_to_database=new_entry(title,description)
    items=get_information()
    return render_template("item_list.html", **locals())

# I should find a better way of getting the items, not by title, I need an id or pk.
# For a shopping list I wouldn't have the same title for two items but even so...
@app.route("/item_delete/<string:title>",methods=["GET", "POST"]) # I should find a better
def get_item_delete(title):
    delete=delete_entry(title)
    items=get_information()
    return render_template("item_list.html", **locals())


@app.route("/list_delete",methods=["GET", "POST"])
def get_list_delete():
    delete_all()
    return render_template("item_list.html", **locals())


if __name__=='__main__':
    app.run(debug=True)
