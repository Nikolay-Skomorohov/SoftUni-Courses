#! python3

# autoStringMailer.py - script that emails a string to the specified address

import re, sys, os, bs4, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

# Navigate the browser to the email webpage

driver.get('https://www.abv.bg/')

# Log in via the credentials

# Log in the user name

userElem = driver.find_element_by_id('username')
userElem.send_keys('python_auto@abv.bg')

# Log in the password

passElem = driver.find_element_by_id('password')
passElem.send_keys('huskarl2006')
passElem.submit()

# Write the email with the specified string

time.sleep(3)
writeNew = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[3]/div')
writeNew.click()
addressElem = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/input')
addressElem.send_keys('nikolai_skomorohov@yahoo.com')
subjectElem = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[5]/td[2]/div/input')
subjectElem.send_keys('Auto Python Tests')
time.sleep(1)
textElem = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/iframe')
textElem.send_keys(sys.argv[1:])

# Send the email

driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[1]/div[1]').click()
driver.quit()
print('Done.')
