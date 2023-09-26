from flask import Flask, render_template, request, redirect, url_for,session
import datetime
import search
import pandas as pd
import TTMScript as GPT
app = Flask(__name__)

@app.route('/locate')
def locate():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        if request.form['brand']!='Device Brand':
            if request.form['model']!='Model Name':
                device_data=search.device_spec(request.form['brand'],request.form['model'],1).to_string
                print(device_data)
                data=GPT.run_query(str(request.form['brand'])+str(request.form['model']),'INR')
                return render_template('index.html',data=data)
    return render_template('index.html',data=False)

if __name__ == "__main__":
    app.run(debug=True)