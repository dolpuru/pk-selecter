from flask import Blueprint

sample_api = Blueprint("sample_api", __name__)


print("a")
import b  # 얘를 제외하고
