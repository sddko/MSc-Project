from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://webscraper.io/test-sites/tables/tables-semantically-correct")

data = []
row = []



tbody = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]")

with open('file.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    

    for tr in tbody.find_elements(By.XPATH, '//tr' ):
        print(tr.text)
        row.clear()
        for item in tr.find_elements(By.TAG_NAME, "td") :
            row.append(item.text)          
        print(row)
        writer.writerow(row)
        print("row loaded")
        
 
time.sleep(5)

driver.quit()

    
        
   
   
'''for item in tr.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/table[1]/tbody/tr/td'):
        row.append(item.text)
        print("new elm")
        print(tr.text) '''






'''
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "W0wltc"))
)
cookiebtn = driver.find_element(By.ID, "W0wltc")
cookiebtn.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("bomber jacket" + Keys.ENTER)



time.sleep(3)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "jacket"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "jacket")
link.click()
'''

