from DataScrape import *
from Database import Query

provinces = GetProvinces()


for province in provinces:
    Query(f"INSERT INTO provinces (id,name) VALUES({province['value']},'{province['name']}')")
    districts = GetProvinceDistricts(province)
    for district in districts:
        Query(f"INSERT INTO districts (id,name,province_id) VALUES({district['value']},'{district['name']}',{province['value']})")
        divisions = GetDistrictDevisions(district)
        for division in divisions:
            Query(f"INSERT INTO divisions (id,name,district_id) VALUES({division['value']},'{division['name']}',{district['value']})")
            
