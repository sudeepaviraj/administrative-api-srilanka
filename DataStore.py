from DataScrape import *
from Database import Query

provinces = GetProvinces()


for province in provinces:
    if(province['name'][0]==" "):
        Query(f"INSERT INTO provinces (id,name) VALUES({province['value']},'{province['name'][1:]}')")
    else:
        Query(f"INSERT INTO provinces (id,name) VALUES({province['value']},'{province['name']}')")
    districts = GetProvinceDistricts(province)
    for district in districts:
        if(district['name'][0]==" "):
            Query(f"INSERT INTO districts (id,name,province_id) VALUES({district['value']},'{district['name'][1:]}',{province['value']})")
        else:
            Query(f"INSERT INTO districts (id,name,province_id) VALUES({district['value']},'{district['name']}',{province['value']})")
        divisions = GetDistrictDevisions(district)
        for division in divisions:
            if(division['name'][0]==" "):
                Query(f"INSERT INTO divisions (id,name,district_id) VALUES({division['value']},'{division['name'][1:]}',{district['value']})")
            else:
                Query(f"INSERT INTO divisions (id,name,district_id) VALUES({division['value']},'{division['name']}',{district['value']})")