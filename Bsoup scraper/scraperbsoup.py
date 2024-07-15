from bs4 import BeautifulSoup
import requests
import csv

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
response = requests.get(url)
#with open("TestSite.html", "r") as f

soup = BeautifulSoup(response.content, 'html.parser')
# doc = BeautifulSoup(f,"html.parser")


# Find elements containing the "$" sign
costs = soup.find_all(string=lambda text: text and "$" in text)
desc = soup.find_all('p', class_="description card-text")
name= soup.find_all('a', class_='title')
print(name)

row1, row2,row3 = [] , [] , []

# Print the extracted costs
print("fetching...")
for cost, dsc, nam in zip(costs , desc, name):
    print(nam['title'] ,"| priced at: ",cost,'| specification: ',dsc.text)

    row1.append(nam['title'])
    row2.append(dsc.text)
    row3.append(cost.text)
    


with open('fileBsoup.csv', 'w', newline="") as file:
    print("Saving file")
    writer = csv.writer(file)
    writer.writerow(row1)
    writer.writerow(row2)
    writer.writerow(row3)




   

#print(doc.prettify())
