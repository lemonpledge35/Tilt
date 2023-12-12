import numpy as np
from flask import Flask, render_template, request
import datetime
import threading

global brewing
brewing = False


class Brew():
    def __init__(self,name):
        self.name = name
        
def get_values():
    t = 75
    sg = 1004
    return t,sg

def begin_brew(fn):
    global brewing
    brewing = True
    beer = Brew(fn)
    return beer

def end_brew():
    global brewing
    brewing = False
    


app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    global brewing
    t,s = get_values()
    #t = datetime.datetime.now().strftime("%H:%M:%S")
    if request.method == 'POST':
        if 'beginbrew' in request.form:
            fn = request.form['beerName']
            beer = begin_brew(fn)
        elif 'endbrew' in request.form:
            end_brew()

        get_values()
        t,s = get_values()
        if brewing:
            bs = f'Brewing {beer.name}'
        else:
            bs = 'Not Brewing'
        return render_template('home.html',temp=t,sg=s,brewing_status=bs)
    
    if request.method == 'GET':
        if brewing:
            return render_template('home.html',temp=t,sg = s,brewing_status = 'Brewing')
        else:
            return render_template('home.html',temp=t,sg=s,brewing_status='Not Brewing')
    


@app.route("/test/")
def rest():
	return render_template('test.html')
