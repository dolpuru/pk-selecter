from flask import Blueprint
from b import deco


sample_api = Blueprint("sample_api", __name__)
deco(sample_api)
print("sample_api")
