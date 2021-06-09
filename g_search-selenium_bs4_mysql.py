#!/usr/bin/env python
# coding: utf-8

# In[1]:


#initialize
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import mysql.connector
import datetime as dt
from datetime import datetime
import time

#fetch data from db
mydb = mysql.connector.connect(
host='localhost',
port=8111,
user='root',
passwd='',
database='web_crawl'
)
mycursor = mydb.cursor()
query = "select keywordId, keywordName from list_kw"
mycursor.execute(query)
data_item = mycursor.fetchall()
mycursor.close()

#input data to list
keyword = []
for data in data_item:
    keyword.append((data[0], data[1]))
mydb.close()

#initialize
targetLink = "https://www.google.com/"
driver = webdriver.Chrome()
driver.get(targetLink)
time.sleep(1)
g_link = []

for i in range(len(keyword)):
    #search the keyword 1 by 1
    tag = keyword[i][1]
    tagId = keyword[i][0]
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(tag + Keys.ENTER)

    #setup to get link(s) question on google
    exclude_link = []
    soup = bs(driver.page_source,'lxml')
    exclude_container = soup.findAll("div",{"class":"ygGdYd related-question-pair"})
    for j in exclude_container:
        container = j.find("a")
        if container==None:
            pass
        else:
            container_2 = container.get("href")
        if "http" in container_2:
            exclude_link.append(container_2)
        else:
            pass
    exclude_link = list(dict.fromkeys(exclude_link))

    #setup to get needed link(s)
    link_container = []
    soup = bs(driver.page_source,'lxml')
    g_body = soup.findAll("div",{"class":"yuRUbf"})
    for j in g_body:
        container = j.findAll("a")
        for j in container:
            container = j.get("href")
            if container==None:
                pass
            link_container.append(container)
            break
            
    for links in link_container:
        timeCrawled = time.strftime('%Y-%m-%d %H:%M:%S')
        
        #when there's no more question link, input to db
        if links not in exclude_link:
            mydb = mysql.connector.connect(
            host='localhost',
            port=8111,
            user='root',
            passwd='',
            database='web_crawl'
            )
            mycursor = mydb.cursor()
            ins_query = '''
                    insert into item_link(
                    keywordId,
                    itemLink,
                    timeCrawled
                    )values(
                    %s,
                    %s,
                    %s)
                    '''
            values = (
                    tagId,
                    links,
                    timeCrawled
                    )
            mycursor.execute(ins_query, values)
            mydb.commit()
            mycursor.close()
            mydb.close()
            time.sleep(3)
    time.sleep(1)
    
    #clear the search bar
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").clear()


# In[ ]:




