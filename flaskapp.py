from flask import Flask, render_template,request,redirect,url_for,send_from_directory,current_app,make_response
import sys
import random
import json

app = Flask(__name__)

@app.route('/')
def loadFile():
    f =open('/home/ubuntu/flaskapp/static/data2.csv', 'a')
    with open('/home/ubuntu/output5/part-00000', 'rb') as csvfile:
        f.write("word1,word2,count")
        for row in csvfile:
            f.write(row)
    return render_template("index.html")
 
@app.route('/bar', methods=['GET','POST'])
def drawbar():
    return render_template("barChart.html")

@app.route('/scatter', methods=['GET','POST'])
def drawscatter():
    return render_template("scatterPlot.html") 
             

if __name__ == '__main__':
    app.run()
