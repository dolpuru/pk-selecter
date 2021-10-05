from flask import render_template, app
from app.api.views_api import views_deco

@views_deco
@app.route('/main')
def index():
    return render_template("index.html")
