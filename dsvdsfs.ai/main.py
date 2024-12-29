#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/advice')
def advice():
    return render_template('advice.html')
 
@app.route('/text')
def text():
    return render_template('text.html')




    
app.run(port=80)