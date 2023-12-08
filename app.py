import numpy as np
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
	t = datetime.datetime.now().strftime("%H:%M:%S")
	return render_template('home.html',current_time=t)

@app.route("/test/")
def rest():
	return render_template('test.html')
