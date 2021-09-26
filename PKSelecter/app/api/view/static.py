"""
static Example API
"""
from flask import Blueprint, render_template

static = Blueprint('static', __name__, route ="/")


@static.route('/')
def index():
    return render_template('index.html')