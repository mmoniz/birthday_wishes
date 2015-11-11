from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Open up the browser
#driver = webdriver.Chrome()

#The easiest way to hide the browser is to install PhantomJS.
driver = webdriver.PhantomJS()

url = "https://www.facebook.com/events/birthdays"
user_email = 'your email'
user_pass = 'your pasword'
msgL = ['Happy Birthday :)','Many happy returns of the day :)','HBD :)']
waitTime = 10


class FacebookBirthdayWishes:

	def __init__(self, driver,url,email,password,msg):
		self.driver = driver
		self.url = url
		self.email = email
		self.password = password
		self.msg = msg

	def navigate(self,url):
		self.driver.get(url)

	def login(self,email,password,driver):
		try:
			emailelement = self.driver.find_element_by_name('email')
			passwordelement = self.driver.find_element_by_name('pass')
			emailelement.send_keys(self.email)
			passwordelement.send_keys(self.password)

			#logging in to the facebook using Selenium
			emailelement.send_keys(Keys.RETURN)

		except Exception as inst:
			print type(inst)     # the exception instance
			print inst.args      # arguments stored in .args
			print inst 
			print "Please check your credential again."

	def wishPeopleHappyBirthday(self,driver,msg):
		statuselement = self.driver.find_elements_by_xpath("//*[@id=\"events_birthday_view\"]/div[1]/div[2]//*")
	
		#posting to the facebook
		for el in statuselement:
			if 'textarea' in el.tag_name:
				#Randomly picks up one of the message from msg
				randomMsg = (random.choice(self.msg))
				el.send_keys(randomMsg)
				el.submit()

	def browserClose(self,driver):
		self.driver.close()

	def browserWaitUntilForConditon(self,driver,time):
		try:
			element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.ID, "events_birthday_view")))
		except:
			print "Couldn't find birthday page, Please check the url"
			driver.quit()


#Navigating to the url
facebookBirthdayWishes = FacebookBirthdayWishes(driver,url,user_email,user_pass,msgL)
facebookBirthdayWishes.navigate(url)

# Logging in facebook by using email and password
facebookBirthdayWishes.login(user_email,user_pass,driver)
facebookBirthdayWishes.browserWaitUntilForConditon(driver,waitTime)

# Wishing Birthday
facebookBirthdayWishes.wishPeopleHappyBirthday(driver,msgL)

# Closing the current Browser
facebookBirthdayWishes.browserClose(driver)
