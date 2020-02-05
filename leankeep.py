# -*- coding: utf8 -*-

import key
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time

def leankeep_a():

	secs = 1
	username_xpath = '//*[@id="ctl00_PageContent_UserName1"]'
	password_xpath = '//*[@id="ctl00_PageContent_Password"]'
	button_id = 'ctl00_PageContent_OKButton__Button'

	driver = webdriver.Firefox()
	driver.get("https://seguro.leankeep.com/leankeepX4/Security/SignIn.aspx")
	time.sleep(secs)

	user_field = driver.find_element_by_xpath(username_xpath)
	time.sleep(secs)
	user_field.send_keys(Keys.CONTROL + "a")
	time.sleep(secs)
	user_field.send_keys(Keys.DELETE)
	time.sleep(secs)
	user_field.send_keys(key.username)

	pass_field = driver.find_element_by_xpath(password_xpath)
	time.sleep(secs)
	pass_field.send_keys(Keys.CONTROL + "a")
	time.sleep(secs)
	pass_field.send_keys(Keys.DELETE)
	time.sleep(secs)
	pass_field.send_keys(key.password)
	time.sleep(secs)

	driver.find_element_by_id(button_id).click()

	print("eita")
	

leankeep_a()