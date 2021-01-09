# Machine-Learning-Project2020
## Project2020
My submission for the Project2020 for Machine Learning and Statistics module at GMIT.

### Lecturer
Dr. Ian McLoughlin
### Student
Freha Saleem
## Project Description
The project goal is to  create a web service that uses machine learning to make predictions based on the data set powerproduction.csv to produce a model that accurately predicts wind turbine power output from wind speed
values, as in the data set.

## About this Repository
This repository contain
- Project2020.ipynb a jupyter notebook containing the data exploration and model fitting
- web-service.py A flask app server
- Templates folder contain the index .html file
- models files
- requirement.text file have information about the packages needed for the app
- Dockerfile configuration for docker
-.gitignore
- .dockerignore

## How to clone this repository
- Go to GitHub.
- Go to  repository: https://github.com/Freeha-S/Machine-Learning-Project2020
- Click the Code button.
- Click on HTTPS and copy the link that is shown.
- Open the command line on your machine, navigate to the directory where you would like to clone the repository down to.
- Enter the command: git clone followed by the URL of the repository.
- The repository will be cloned down to your current working directory.
Accessing the Web App
In order to open the web app localy, clone or download this github repository (keep the directory structure intact).

## Option 1)To Run the App in Virtual environment

The following steps depend on the operating system.

## A) Linux

- Within the directory, create a new virtual environment, typing in the terminal
~~~~code
python -m venv venv
~~~~
Activate the virtual environment:

~~~~code
source venv/bin/activate 
~~~~
Install all the required libraries listed in the requirements.txt file:

~~~~
pip install -r requirements.txt
~~~~
Start the web app using the command:

~~~~
export FLASK_APP=web-service.py
To run the server program, type:
python -m flask run
This will activate localhost server at http://127.0.0.1:5000/.
~~~~
To stop the server running, press ctrl+c in terminal.

In order to leave the virtual environment:
~~~~
deactivate
~~~~
B) Windows

Within the directory, create a new virtual environment, typing in the terminal

~~~~code
python -m venv venv
~~~~
Activate the virtual environment:

~~~~code
\venv\Scripts\activate.bat
~~~~
Install all the required libraries listed in the requirements.txt file:

~~~~code
pip install -r requirements.txt
~~~~
To run the server program, type:

~~~~code
set FLASK_APP=web-service.py
~~~~
To run the server program, type

~~~~code
flask run
~~~~
 This will activate localhost server at http://127.0.0.1:5000/.

To stop the server running, press ctrl+c in terminal.

In order to leave the virtual environment:

~~~~code
deactivate
~~~~
Option 2) Docker

- Install Docker on your computer, typing in the terminal:

Inside the directory holding the repository, run the following commands to build a docker image

~~~~code
docker build . -t power-app
~~~~
In order to create and start the docker container, execute the command:

~~~~code
docker run --name power-container -d -p 5000:5000 power-app
~~~~
This will activate localhost server at http://127.0.0.1:5000/.

To stop the server running, press ctrl+c in terminal.
