#asyncclientcsv.py
#65.9 seconds to scrape to a csv without multiprocessing, 27 seconds with 16 processor pools, 32 seconds with 8, 35 with 16 again, 25.7 seconds at 16 pools



#get all urls to scrape first

#then get data

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import asyncio
import aiohttp
from multiprocessing import Pool
import re
import time
scrpdata = []
cost = []
name= []
score = []


baseurl = 'https://books.toscrape.com/'
response = requests.get(baseurl);
pg = 1;
soup = BeautifulSoup(response.content , 'html.parser'); 
nxt = True


links = [] 
pglinks = []
output =[]


#1st function gets data off page,
#put all task together
#main func which controls everything which we give all urls too
async def get_page(session, url):
    #use the try function here for error handling
    try:
        async with session.get(url) as r:
            return await r.text()
    except:
        print('site request time out')
        return None


async def get_all(session, urls):
    #use the try function here for error handling
    tasks = []
    try:
        for url in urls:
        
            task = asyncio.create_task(get_page(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results
    except:
        print('async function error, check list of urls')


async def main(urls):
    #use the try function here for error handling for incorrect url
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        return data


def parse(results): #
    #print function for finding stuff on a page
    #use the try function here for error handling here based on improper results
    for html in results:

        soup = BeautifulSoup(html, 'html.parser')
        
        try:
            name.append(soup.find('img', alt=True)['alt'])
        except:
            print('name not found, check url: ')
        try:
            cost.append(soup.find('p', class_='price_color').text)
        except:
            print('cost not found, check parameters of cost element: ')
        try:
            score.append(soup.find('p', class_='star-rating')['class'][1])
        except:
            print('score unavailable, check tag details ')


    



   
#non async functions below

def strt_tm():
    return time.time()

def stp_tm(start_time):
    elapsed_time = time.time() - start_time
    return elapsed_time


def storfunc():# for storing data
    global scrpdata
    print('storing values column wise in a csv file')
    for i in range(len(name)):
        scrpdata.append([name[i], cost[i], score[i]])
    df = pd.DataFrame(scrpdata , columns=['name','cost','score'])

    df.to_csv('asyncdata.csv')

def loadpage(url):
    #use the try function here for error handling
    global response
    global soup
    if url == False:
        print('no more pages left to scrape')
    else:
        try:
            response=requests.get(url);
            soup=BeautifulSoup(response.content, 'html.parser')
        except:
            print('link not found, check URL conditions for missing words like -catalogue-')
    
def findnxtpage():
    #use the try function here for error handling
    global nxt 
    global pg
    print('checking if next pg exists')
    nxt = soup.find('a', string='next')
    
    if nxt:
        pg+=1
        return(baseurl + f'catalogue/page-{pg}.html')
    else:
        return(False)
    print(pg)



    
def getlinks(url):#used function
    #use the try function here for error handling for finding
    global ti
    global links
    global pglinks
   #finds all links for books on a page
    try:
        response=requests.get(url);
        soup=BeautifulSoup(response.content, 'html.parser')
    except:
        print('invalid URL or network time out')
    
    try:
        ti = soup.find_all('a', title=True)
        for title in ti:
            global links
            links.append('https://books.toscrape.com/catalogue/' + title['href'])
        return(links)
    except: print('product link not found at the following url: ', url)
    

def un_nestlist(li): #used function
        for i in li:
            if type(i) == list:
                un_nestlist(i)
            else:
                output.append(i)


def maxpgfetch():#fetches all pages till the last one
    try:
        pgs =  soup.find('li', class_='current').text #finds max number of pages to be iterated through
        mpg = re.sub('Page 1 of', '', pgs)
        print('number of next pages to scroll through: ',  int(mpg))
        for pg in range (1,int(mpg)+1 ):
            pglinks.append(baseurl + f'catalogue/page-{pg}.html')
    except:
        print('max number of pages to scroll through not found, check logic and page elements')








if __name__ == '__main__':
    startTime = strt_tm()
    maxpgfetch()

    with Pool(16) as pool:
        print('fetching pool')
        results = (pool.map(getlinks, pglinks ))
    print('test')
    print(len(results))
    un_nestlist(results)




    print(len(output))
    output = list(dict.fromkeys(output)) #removing any duplicates
    

    
    print('amount of entries: ' , len(output))

    elapsedTime = stp_tm(startTime)

    print('executed in: ', elapsedTime)
    print(f"Elapsed time for gathering and constructing urls: {elapsedTime:.6f} seconds")

    startTime = strt_tm()




    results = asyncio.run(main(output)) #fetch

    parse(results) #find

    storfunc() # store

    print('scraped')
    elapsedTime = stp_tm(startTime)

    print('executed in: ', elapsedTime)
    print(f"Elapsed time for gathering html, preprocessing, finding elements and storing them: {elapsedTime:.6f} seconds")

  




