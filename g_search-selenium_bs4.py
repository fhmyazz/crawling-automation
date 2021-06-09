#!/usr/bin/env python
# coding: utf-8

# In[1]:

#initialize
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

g_link = []
targetLink = "https://www.google.com/"
keyword = ["animals", "stock", "fashion"]
driver = webdriver.Chrome()
driver.get(targetLink)
time.sleep(1)

for tag in keyword:
    #search the keyword 1 by 1
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(tag + Keys.ENTER)

    exclude_link = []
    #setup to get link(s) question on google
    soup = bs(driver.page_source,'lxml')
    exclude_container = soup.findAll("div",{"class":"ygGdYd related-question-pair"})
    for i in exclude_container:
        container = i.find("a").get("href")
        if "http" in container:
            exclude_link.append(container)
        else:
            pass
    exclude_link = list(dict.fromkeys(exclude_link))

    #setup to get needed link(s)
    link_container = []
    soup = bs(driver.page_source,'lxml')
    g_body = soup.findAll("div",{"class":"yuRUbf"})
    for i in g_body:
        y = i.findAll("a")
        for j in y:
            container = j.get("href")
            link_container.append(container)
            break
            
    #exclude link in variable "exclude_link" and add the keyword, for tag purpose
    for x in link_container:
        if x not in exclude_link:
            g_link.append((x, tag))
    time.sleep(1)
    
    #clear the search bar
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").clear()
