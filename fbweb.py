from selenium import webdriver
import time,random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome()
url = "https://www.facebook.com/events/birthdays"
user_email = 'your email'
user_pass = 'your pasword'
msgL = ['Happy Birthday :)','Many happy returns of the day :)','HBD :)']


class BasePage:

	def __init__(self, driver):
		self.driver = driver

	def navigate(self,url):
		self.driver.get(url)

	def browserClose(self,driver):
		self.driver.close()


class FacebookLogin(BasePage):

	def login(self,email,password,driver):
		try:
			self.driver = driver
			self.email = email
			self.password = password
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



class BirthdayWish(BasePage):

	def wishPeopleHappyBirthday(self,driver,message):
		statuselement = self.driver.find_elements_by_xpath("//*[@id=\"events_birthday_view\"]/div[1]/div[2]//*")
		#posting to the facebook
		for el in statuselement:
			if 'textarea' in el.tag_name:
				el.send_keys(message)
				el.submit()


#Navigating to the url
basePage = BasePage(driver)
basePage.navigate(url)
time.sleep(3)

# Logging in facebook by using email and password
facebookLogin = FacebookLogin(driver)
facebookLogin.login(user_email,user_pass,driver)
time.sleep(3)

#Randomly picks up one of the message from msgL
randomMsg = (random.choice(msgL))

# Wishing Birthday
birthdayWish = BirthdayWish(driver)
birthdayWish.wishPeopleHappyBirthday(driver,randomMsg)
time.sleep(3)

# Closing the current Browser
basePage.browserClose(driver)


