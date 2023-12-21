import numpy as np
from flask import Flask, render_template, request
import datetime
import threading
import read

global brewing
global beer
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
    global beer
    brewing = True
    beer = Brew(fn)
    run()

def end_brew():
    global brewing
    brewing = False
    
def run():
    global brewing
    global beer
    file_name = f'data/{beer.name}.txt'
    open(file_name,'w')
    close(file_name)
    while brewing:
        temp, sg = read.get_values()
        time = datetime.datetime.now()
        with open(file_name,'a') as f:
            f.write(time,',',temp,',',sg,',')
        time.sleep(600)
        
        

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    global brewing
    global beer
    t,s = read.get_values()
    #t = datetime.datetime.now().strftime("%H:%M:%S")
    if request.method == 'POST':
        if 'beginbrew' in request.form and not brewing:
            beer_name = request.form['beerName']
        elif 'endbrew' in request.form and brewing:
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
def test():
    with open('test.txt','w') as f:
        f.write('apple')
	return render_template('test.html')
