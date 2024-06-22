from flask import Flask, render_template, request, url_for, redirect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random
import os

app = Flask(__name__)
port = os.getenv("PORT")

uri = "mongodb+srv://srivardhanvuralearns:eb1Vrtzkq8dCKexN@cluster0.uaji4wp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        mydb = client["db"]
        mycol = mydb["users"]
        mydict = {"username": username, "password": password}
        x = mycol.insert_one(mydict)
        # print(x)
    except Exception as e:
        print(e)
    return redirect(url_for('actor'))


@app.route('/home')
def actor():
    colors = ["Red", "Blue", "Green", "Black", "Yellow"]
    images = [
        "static/images/red.jpg",
        "static/images/blue.jpg",
        "static/images/green.png",
        "static/images/black.jpg",
        "static/images/yellow.avif",
    ]
    i = random.randint(0, len(colors) - 1)
    data = {"name": colors[i], "image_url": images[i]}
    return render_template('actors.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
