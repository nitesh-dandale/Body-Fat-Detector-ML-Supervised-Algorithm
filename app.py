# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest Regressor model
filename = 'bodyfat.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        neck = float(request.form['neck'])
        chest = float(request.form['chest'])
        abdomen = float(request.form['abdomen'])
        hip = float(request.form['hip'])
        thigh = float(request.form['thigh'])
        knee = float(request.form['knee'])
        ankle = float(request.form['ankle'])
        biceps = float(request.form['biceps'])
        forearm = float(request.form['forearm'])
        wrist = float(request.form['wrist'])


        data = np.array([[age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm,wrist]])
        my_prediction = classifier.predict(data)
        output = round(my_prediction[0], 2)
        if output>25:
            bodyfatnumber = 1
        else:
            bodyfatnumber = 0
        if output < 0:
            return render_template('index.html', prediction_text="Sorry you entered invalid numbers")
        else:
            return render_template('index.html', prediction_text=output, bodyfat = bodyfatnumber)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)