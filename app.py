from flask import Flask, render_template,redirect, request, jsonify
import sqlite3
from engine import *

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/item_list",methods=["GET"])
def get_item_list():
    items=get_information()
#    for item in items:
#        title=item[0]
#        description=item[1]
    return render_template('item_list.html', **locals())

@app.route("/item_new",methods=["GET", "POST"])
def get_item_new():
    form_data = request.form
    title=form_data["title"]
    description=form_data["description"]
    new_to_database=new_entry(title,description)
    return render_template("index.html", **locals())


@app.route("/item_delete/<string:title>",methods=["GET", "POST"])
def get_item_delete(title):
    delete=delete_entry(title)
    return render_template("index.html", **locals())


@app.route("/list_delete",methods=["GET", "POST"])
def get_list_delete():
    delete_all()
    return render_template("item_list.html", **locals())


if __name__=='__main__':
    app.run(debug=True)
