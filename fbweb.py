import webbrowser
import requests, bs4
import urllib3 
from selenium import webdriver
import re,sys
from selenium.webdriver.common.keys import Keys
import time

#url = 'http://www.facebook.com'

# Open URL in new browser window
#webbrowser.open_new(url) # opens in default browser



from splinter import Browser

def happy (driver, url):
	print url
	driver.get(url)

	elem = driver.find_element_by_class_name('_3br6')
	elem.click()

	elem.send_keys("Happy birthday")

	elem.send_keys(Keys.RETURN)

def findUrl(driver):
	brow = driver.find_element_by_class_name('_cwn')
	obj = re.findall(r"href=\"https://www.facebook.com/[\w*.]+",brow.get_attribute("outerHTML"))
	#print obj
	return obj

#user_email = raw_input("enter users email address ")
#user_pass = raw_input("enter users password ")
user_email = 'flora_ripudaman@hotmail.com'
user_pass = 'Pavi1517'
#browser= Browser('firefox')

driver = webdriver.Firefox()

driver.get('https://www.facebook.com/events/birthdays')

#browser.fill('email', user_email)
elem = driver.find_element_by_name('email')
elem.send_keys(user_email)

elem = driver.find_element_by_name('pass')
elem.send_keys(user_pass)

elem.send_keys(Keys.RETURN)

time.sleep(3)


happy(driver, "https://www.facebook.com/melissa.athena")

#obj = findUrl(driver)

#for names in obj:
#	happy(names.split("href=\"")[1])

