from flask import Flask, request, jsonify, render_template, json

from urllib.request import urlopen,Request,urlretrieve
import datetime, os, webbrowser, csv, requests, urllib.request, random
import sqlite3

import logging

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/gettemperature', methods=['POST'])
def gettemperature():
    zipcode = request.form['zip']
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=0bfdb889cbb648fab0ac52f70199760e')
    json_object = r.json()
    tempk= float(json_object["main"]["temp"])
    tempf = (tempk -273.15)*1.8+32
    return render_template('temperature.html',temp=tempf)

if __name__=='__main__':
    app.run(debug='true')