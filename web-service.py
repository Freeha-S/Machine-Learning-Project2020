import os
#import flask for web app
import flask as fl
# Numpy for numerical arrays.
import numpy as np
# pickle for saving and restoring ML models.
import joblib
# For restoring a keras model.
from tensorflow.keras.models import load_model
from flask import render_template,request,send_from_directory
from sklearn.preprocessing import PolynomialFeatures

t=10
#Import Models

#Import polynomial regression model.
#polyreg3 = joblib.load("poly_reg.pkl")
polyreg = joblib.load("models/poly_reg5.pkl")
#polynomial_features= PolynomialFeatures(degree=5)
#x_poly = polynomial_features.fit_transform(np.array([10]).reshape(1,-1))
#p = polyreg.predict(x_poly)
#print(p) # check if it is working fine

#Import Random Forst Model.
randomForest = joblib.load("models/randomF_model.pkl")

#print(randomForest.predict(([[10]])))

#Import Neural Network model.
neuralNetwork = load_model("models/neural_model.h5")
#Xnew = array([[0.29466096, 0.30317302]])
#https://machinelearningmastery.com/how-to-make-classification-and-regression-predictions-for-deep-learning-models-in-keras/
#p= neuralNetwork.predict([[10]])
#print(p)

#Create a web app
app = fl.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# curl 127.0.0.1:5000/api/model1/15
@app.route('/api/model1/<float:s>')
@app.route('/api/model1/<int:s>')
def model1(s):
    #https://towardsdatascience.com/polynomial-regression-bbe8b9d97491
    #code for getting right shape input adopted from https://stackoverflow.com/a/55197421
    polynomial_features= PolynomialFeatures(degree=5, include_bias=False)
    x_poly = polynomial_features.fit_transform(np.array([s]).reshape(1,-1))
    p = polyreg.predict(x_poly)
    # return predicted value
    app.logger.info("model1")
    return {"value": str(p[0])} 

# curl 127.0.0.1:5000/api/model2/15
@app.route('/api/model2/<float:s>')
@app.route('/api/model2/<int:s>')
def model2(s):
    p = randomForest.predict(([[s]]))
     # return predicted value
    app.logger.info("model2")
    return {"value": str(p[0])} 
    
# curl 127.0.0.1:5000/api/model3/15
@app.route('/api/model3/<float:s>')
@app.route('/api/model3/<int:s>')
def model3(s):
    # Make the prediction model
    p = neuralNetwork.predict([[s]])
    #return the predicted value
    app.logger.info("model3")
    return {"value": str(p[0][0])} 

@app.route('/favicon.ico')
def favicon():
    return  render_template('index.html')  


# Run in debug mode
if __name__ == "__main__":
   app.run(debug=True)

#https://towardsdatascience.com/polynomial-regression-bbe8b9d97491