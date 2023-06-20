from flask import Flask
import json
from DataScrape import GetProvinces

app = Flask(__name__)

@app.route("/provinces")
def ProvincesList():
    return json.dumps(GetProvinces(),indent=2)