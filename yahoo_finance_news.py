# import packege
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

# Initialize values
url = "https://finance.yahoo.com/topic/stock-market-news"
links = [] 
headers = {'accept-ranges':'bytes',
          'access-control-allow-origin':'*',
          'content-encoding': "gzip",
          'cache-control': 'private, max-age=86400',
          'content-type':'text/javascript'}
info = []

# Get Links function
def get_links(url):
    driver = webdriver.Chrome(r'C:\Users\User\chromedriver')
    driver.get(url)
    
    element = driver.find_element(By.XPATH, "//div[@id='Col2-6-LinkOut-Proxy']")

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
        
    all_a = driver.find_elements(By.XPATH, '//h3[@class="Mb(5px)"]//a')

    for a in all_a: 
        if a.get_attribute('href') not in links:
            links.append(a.get_attribute('href'))
                
                
    driver.close()
    print("Number of links that are gathered : {}".format(len(links)))
    
    return links


# get info function
def get_info(url):
    #grab the information
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    news = soup.find('div', attrs={'class': 'caas-body'}).text
    headline = soup.find('h1').text 
    date = datetime.strptime(soup.find('time').text, "%B %d, %Y, %I:%M %p")
    
    #combine all info into a list of columns
    columns = [news, headline, date, url]
    #give columns names
    column_names = ['News','Headline','Date', 'Url']
    
    return dict(zip(column_names, columns))


# main process
links =  get_links(url)
for link in links:
    try:
        scraped = get_info(link)
        info.append(scraped)
        time.sleep(3)
        
    except requests.exceptions.ConnectionError:
        print("Connection refused by the server..")
        print("Let me sleep for 3 seconds")
        print("ZZzzzz...")
        time.sleep(3)
        print("Was a nice sleep, now let me continue...")

df = pd.DataFrame(info)
df.to_csv("finance_yahoo_news.csv", index=False)
