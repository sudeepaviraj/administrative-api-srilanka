from flask import Flask,jsonify
import json
from flask import request
from Database import SelectQuery

app = Flask(__name__)

@app.route("/provinces",methods=["GET"])
def ProvincesList():
    provinces = SelectQuery("SELECT * FROM provinces")
    print(json.dumps({"provinces":provinces}))
    return json.dumps(provinces)

@app.route("/districts",methods=["GET"])
def DistrictsList():
    districts= SelectQuery("SELECT id,name FROM districts")
    return json.dumps(districts)

@app.route("/getdistricts",methods=["GET"])
def DistrictsListSELECT():
    id = request.args.get("province")
    if id is None:
        return "Please Add Province Id",422
    else:
        districts = SelectQuery(f"SELECT id,name FROM districts WHERE province_id = {id}")
        print(districts)
        return districts

@app.route("/divisions",methods=["GET"])
def DivisionsList():
    divisions= SelectQuery("SELECT id,name FROM divisions")
    return json.dumps(divisions)

@app.route("/getdivisions",methods=["GET"])
def DivisionsListSELECT():
    id = request.args.get("district")
    if id is None:
        return "Please Add District Id", 422
    else:
        divisions = SelectQuery(f"SELECT id,name FROM divisions WHERE district_id = {id}")
        return json.dumps(divisions)


if __name__ == "__main__":
    app.run(debug=True)