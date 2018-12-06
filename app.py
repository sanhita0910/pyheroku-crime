import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import time
from datetime import datetime
from sklearn import tree

from flask import Flask, jsonify, render_template

app = Flask(__name__)

##########
# HOME PAGE 
##########
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
##########


if __name__ == "__main__":
    app.run(debug=True)