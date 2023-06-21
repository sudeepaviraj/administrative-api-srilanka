from fastapi import FastAPI
from Database import SelectQuery
import json

app = FastAPI()


@app.get("/provinces")
async def ProvincesList():
    provinces = SelectQuery("SELECT * FROM provinces")
    print(provinces)
    return provinces
@app.get("/districts")
async def DistrictsList():
    districts = SelectQuery("SELECT id,name FROM districts")
    return districts

@app.get("/divisions")
def DivisionsList():
    divisions= SelectQuery("SELECT id,name FROM divisions")
    return divisions
