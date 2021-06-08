#!/usr/bin/env python
# coding: utf-8

# In[1]:


#initialize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import mysql.connector
import time

targetLink = "https://www.google.com/"
keyword = ["animals", "stock", "fashion"]
driver = webdriver.Chrome()
driver.get(targetLink)
time.sleep(1)

#loop for each keyword
for i in keyword:
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(i + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").clear()

