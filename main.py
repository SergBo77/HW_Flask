from flask import Flask, render_template
import time
import tkinter as tk

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

@app.route("/time/")
def time():
    return render_template('time.html')

if __name__ == "__main__":
    app.run()