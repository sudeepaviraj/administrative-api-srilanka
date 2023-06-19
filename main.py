from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://apps.moha.gov.lk:8090/lifecode/gn_list")

time.sleep(3)