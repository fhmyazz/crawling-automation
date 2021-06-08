#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd
import mysql.connector
import datetime as dt
from datetime import datetime
import time

g_link = []
targetLink = "https://www.google.com/"
keyword = ["animals", "stock", "fashion"]
driver = webdriver.Chrome()
driver.get(targetLink)
time.sleep(1)

for tag in keyword:
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(tag + Keys.ENTER)

    exclude_link = []
    soup = bs(driver.page_source,'lxml')
    exclude_container = soup.findAll("div",{"class":"ygGdYd related-question-pair"})
    for i in exclude_container:
        container = i.find("a").get("href")
        if "http" in container:
            exclude_link.append(container)
        else:
            pass
    exclude_link = list(dict.fromkeys(exclude_link))

    link_container = []
    soup = bs(driver.page_source,'lxml')
    g_body = soup.findAll("div",{"class":"yuRUbf"})
    for i in g_body:
        y = i.findAll("a")
        for j in y:
            container = j.get("href")
            link_container.append(container)
            break
            
#     links = [x for x in link_container if x not in exclude_link]
    for x in link_container:
        if x not in exclude_link:
            g_link.append((x, tag))
    time.sleep(1)
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").clear()


# In[2]:


g_link


# In[ ]:


a = ["a","b","c"]
b = ["b","c","d"]

for x in a:
    if x not in b:
        print(x)


# In[ ]:


keyword = ["animals", "stock", "fashion"]
for i in keyword:
    print(i)


# In[ ]:


link_container


# In[ ]:


driver.refresh()


# In[ ]:


driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(keyword[1] + Keys.ENTER)


# In[ ]:


driver.find_element_by_class_name("ExCKkf.z1asCe.rzyADb").click()


# In[ ]:


links = [x for x in link_container if x not in exclude_link]
links

