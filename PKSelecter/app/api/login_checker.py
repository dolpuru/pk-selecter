# client - server에 대한 api를 모았습니다.
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/main')
def main():
