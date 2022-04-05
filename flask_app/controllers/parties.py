from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import Party
from flask_app import User


app.router('/all')
