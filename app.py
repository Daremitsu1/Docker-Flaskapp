from flask import Flask, request
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)

# Read the pickle file
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All!"



if __name__ == "__main__":
    app.run()