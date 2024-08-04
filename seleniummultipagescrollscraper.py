from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


# other site for bohoo

#this is a test to make sure scraper is working access wise

driver.get("https://books.toscrape.com/")

time.sleep(2)

print("scraping")

td = driver.find_elements(By.XPATH, '//p[@class="price_color"]')
for pr in td:
   print(pr.text)

count = 1

nxt = driver.find_element(By.XPATH, '//a[ contains (text(), "next" ) ]')

#nxt = driver.find_element(By.LINK_TEXT, 'next' )
while nxt:

    nxt = driver.find_element(By.XPATH, '//a[ contains (text(), "next" ) ]')
    nxt.click()
    count += 1
    print('page ', count)
    td = driver.find_elements(By.XPATH, '//p[@class="price_color"]')
    for pr in td:
        print(pr.text)
    try:
        nxt=driver.find_element(By.XPATH, '//a[ contains (text(), "next" ) ]')

    except:
        break



print("scraped")



driver.quit()

