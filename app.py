from flask import Flask
import json
from DataScrape import GetProvinces
from Database import SelectQuery

app = Flask(__name__)

@app.route("/provinces")
def ProvincesList():
    provinces = SelectQuery("SELECT * FROM provinces")
    return json.dumps(provinces,indent=2)

@app.route("/districts")
def DistrictsList():
    districts= SelectQuery("SELECT id,name FROM districts")
    return json.dumps(districts,indent=2)

@app.route("/divisions")
def DivisionsList():
    divisions= SelectQuery("SELECT id,name FROM divisions")
    return json.dumps(divisions,indent=2)

if __name__ == "__main__":
    app.run(debug=True)