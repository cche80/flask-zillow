from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# create a Flask object which implements a WSGI (Web Service Gateway Interface)
# it will act as a central registry for the view functions, the URL rules, template configuration and much more. Basically a central registry for many many web app activities

# Overhere, we pass it into SQLAlchemy, use db credentials in config.py to create a db object which is a communication channel between the app and the db!
application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)

## This __init__.py is in application folder, which marks the folder as a package in the app hierarchy.

# Name of the packlage: application
# An object (executable statement) that you can import from this package: db
# This package (application) has two other modules you can play with:
# forms.py and models.py
# each module has its own executable statements as well as function definitions.
