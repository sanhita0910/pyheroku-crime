import sys
from flask import Flask, render_template, jsonify, redirect

app = Flask(__name__)

##########
# HOME PAGE 
##########
@app.route('/')
def index():
    print("----------rendering")
    return render_template('index.html')
##########


if __name__ == '__main__':
    app.run(debug=True)
