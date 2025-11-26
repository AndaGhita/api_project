# api_project

# Virtual environments

Create an environment
Create a project folder and a .venv folder within:
 mkdir api_project
 cd api_project
 py -3 -m venv .venv

Activate the environment
Before you work on your project, activate the corresponding environment:
 ..\venv\Scripts\Activate.ps1

# Install Flask
Within the activated environment, use the following command to install Flask:
pip install Flask

# Install dependencies

Install the extension jsonify
pip install flask-jsonpify

# How to run the Flask app

Run the app using the command:
 flask -app main.py run
 python main.py


