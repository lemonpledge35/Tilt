import numpy as np
from flask import Flask, render_template, request
import datetime
import time
import threading
import read
import glob

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
    run_thread = threading.Thread(target=run)
    run_thread.start()

def end_brew():
    global brewing
    brewing = False
    
def run():
    global brewing
    global beer
    file_name = f'data/{beer.name}.txt'
    f = open(file_name,'w')
    f.close()
    while brewing:
        temp, sg = read.get_values()
        time_now = datetime.datetime.now()
        with open(file_name,'a') as f:
            f.write(f'{time_now},{temp},{sg}\n')
        time.sleep(10)
        
        


def get_data_files():
    return glob('data/*')

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
            begin_brew(beer_name)
        elif 'endbrew' in request.form and brewing:
            end_brew()

        get_values()
        t,s = get_values()
        if brewing:
            bs = f'Brewing {beer.name}'
        else:
            bs = 'Not Brewing'
        return render_template('home.html',temp=t,sg=s,brewing_status=bs,
                               files=get_data_files())
    
    if request.method == 'GET':
        if brewing:
            return render_template('home.html',temp=t,sg = s,
                                   brewing_status = 'Brewing',files=get_data_files())
        else:
            return render_template('home.html',temp=t,sg=s,
                                   brewing_status='Not Brewing',files=get_data_files())
    


@app.route("/test/")
def test():
    return render_template('test.html')
