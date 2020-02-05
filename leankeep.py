# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
from mechanize import Browser
import urllib.request
import urllib.parse
import re
import sys
import requests
import mechanize
import keys
from selenium import webdriver

def leankeep_a():

	username_xpath = '//*[@id="ctl00_PageContent_UserName1"]'
	password_xpath = '//*[@id="ctl00_PageContent_Password"]'
	button_id = 'ctl00_PageContent_OKButton__Button'

	driver = webdriver.Firefox()
	driver.get("https://seguro.leankeep.com/leankeepX4/Security/SignIn.aspx")
	driver.implicitly_wait(30)
	driver.find_element_by_xpath(username_xpath).send_keys(keys.username)
	driver.implicitly_wait(30)
	driver.find_element_by_xpath(password_xpath).send_keys(keys.password)
	driver.implicitly_wait(30)
	driver.find_element_by_id(button_id).click()

	print("eita")
	

leankeep_a()