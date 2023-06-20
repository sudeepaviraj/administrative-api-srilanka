from flask import Flask,jsonify
import json
from DataScrape import GetProvinces
from Database import SelectQuery

app = Flask(__name__)

@app.route("/provinces")
def ProvincesList():
    provinces = SelectQuery("SELECT * FROM provinces")
    print(json.dumps({"provinces":provinces}))
    return jsonify({"provinces":provinces})


@app.route("/districts")
def DistrictsList():
    districts= SelectQuery("SELECT id,name FROM districts")
    return json.dumps(districts)

@app.route("/divisions")
def DivisionsList():
    divisions= SelectQuery("SELECT id,name FROM divisions")
    return json.dumps(divisions)

if __name__ == "__main__":
    app.run(debug=True)