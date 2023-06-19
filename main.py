from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://apps.moha.gov.lk:8090/lifecode/gn_list")

provinces = Select(driver.find_element(By.NAME,"province"))

province_count = len(provinces.options)


for province in range(province_count):
    provinces.select_by_index(province)
    print(provinces.first_selected_option.get_attribute("value"))
    districts = Select(driver.find_element(By.NAME,"district"))
    district_count = len(districts.options)
    for district in range(district_count):
        districts.select_by_index(district)
        time.sleep(10)

time.sleep(3)