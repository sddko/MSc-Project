from bs4 import BeautifulSoup
import requests
import csv




pg=1;
url = f'https://books.toscrape.com/catalogue/page-{pg}.html';


response = requests.get(url);

soup = BeautifulSoup(response.content , 'html.parser');

nxt = soup.find('a', string='next');



# while next exists, add a number increment to the link and keep increasing and running the code again
def checknext():
    global nxt 
    nxt = soup.find('a', string='next')


def findprice():
    global soup
    soup = BeautifulSoup(response.content , 'html.parser')
    global pr
    pr = soup.find_all('p', class_='price_color')
    for price in pr:
        print(price.text)

def findurl():
    global url
    url = f'https://books.toscrape.com/catalogue/page-{pg}.html'
    print(url)
    global response
    response = requests.get(url)
    global soup
    soup= BeautifulSoup(response.content , 'html.parser')


def runfunc():
    global nxt
    while nxt:
        findprice()
        checknext()
        global pg 
        if nxt:
            pg += 1
            findurl()
        else:
            break

        

print('starting scrape')
runfunc()
    




    

    
