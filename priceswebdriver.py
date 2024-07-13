from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import numpy as np


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

#data = []
row = []



with open('file.csv', 'w', newline="") as file:
    writer = csv.writer(file)

    row.clear()
    td = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div/h4/a")
    for elem in td:
        row.append(elem.text)
    writer.writerow(row)    

    row.clear()
    td = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div/h4[1]")
    print("running")
    for elem in td:
        row.append(elem.text)
    writer.writerow(row)


    row.clear()
    td = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/p")
    for elem in td:
        row.append(elem.text)
        print(elem.text)
    writer.writerow(row)



    


        
        
        
'''
        row.clear()
        for item in tr.find_elements(By.TAG_NAME, "td") :
            row.append(item.text)          
        print(row)
        writer.writerow(row)
        print("row loaded") '''
        
 


driver.quit()

print("scraped")
        
   
   
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

