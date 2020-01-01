from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def about():
    return render_template('index.html')

@app.route('/fbp')
def fbp():
    return render_template('fbp.html')

@app.route('/dktrm')
def dktrm():
    return render_template('dktrm.html')

@app.route('/ctcrdo')
def ctcrdo():
    return render_template('ctcrdo.html')

@app.route('/fyi')
def fyi():
    return render_template('fyi.html')

app.run(debug=True)