import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


def GetProvinces() -> list:

    ProvinceList = []

    cookies = {
        'lifecode': 'jfal4q3a37c7ql6ukf138g1l4r',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'lifecode=jfal4q3a37c7ql6ukf138g1l4r',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get('http://apps.moha.gov.lk:8090/lifecode/village_list',
                            cookies=cookies, headers=headers, verify=False)

    soup = BeautifulSoup(response.content, "html.parser")

    provinces = soup.find("select")

    for province in provinces:
        if (province.getText()[3:] != 'ect a Province'):
            try:
                ProvinceList.append(
                    {"name": province.getText()[3:], "value": province["value"]})
            except:
                pass
        else:
            pass
    return ProvinceList


def GetProvinceDistricts(province: str) -> list:

    DistrictList = []

    cookies = {
        'lifecode': 'jfal4q3a37c7ql6ukf138g1l4r',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'lifecode=jfal4q3a37c7ql6ukf138g1l4r',
        'Origin': 'http://apps.moha.gov.lk:8090',
        'Referer': 'http://apps.moha.gov.lk:8090/lifecode/village_list',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'action': 'province',
        'query': province["value"],
    }

    response = requests.post(
        'http://apps.moha.gov.lk:8090/lifecode/views/fetch.php',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    soup = BeautifulSoup(json.loads(response.content)["output"], "html.parser")

    districts = soup.find_all("option")

    for district in districts:
        if (district.getText() != "Select a District"):
            try:
                DistrictList.append(
                    {"name": district.getText()[3:], "value": district["value"]})
            except:
                pass
        else:
            pass
    return DistrictList


def GetDistrictDevisions(district):

    DevisonList = []

    cookies = {
        'lifecode': 'jfal4q3a37c7ql6ukf138g1l4r',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'lifecode=jfal4q3a37c7ql6ukf138g1l4r',
        'Origin': 'http://apps.moha.gov.lk:8090',
        'Referer': 'http://apps.moha.gov.lk:8090/lifecode/village_list',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'action': 'district',
        'query': district["value"],
    }

    response = requests.post(
        'http://apps.moha.gov.lk:8090/lifecode/views/fetch.php',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    soup = BeautifulSoup(json.loads(response.content)["output"], "html.parser")

    devisions = soup.find_all("option")

    for devision in devisions:
        if (devision.getText() != "Select a Divisional Secretariat"):
            try:
                DevisonList.append({"name": devision.getText()[
                                   3:], "value": devision["value"]})
            except:
                pass
        else:
            pass
    return DevisonList
