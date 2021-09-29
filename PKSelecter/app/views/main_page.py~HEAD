"""
static API
"""
from flask import Blueprint, render_template
from app.api.view import template_bp

@template_bp.route('/')
def index():
    return render_template("index.html")