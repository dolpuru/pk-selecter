"""
Sample API Module Package
"""
from flask import Blueprint

sample_api = Blueprint('sample_api', __name__)
print(3)
import b
print(2)

# 실행되는 순서 import time, runtime 알아보기