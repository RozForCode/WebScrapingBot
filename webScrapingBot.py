#this program will take search input from the user and and will open amazon
#page related to that search

import time
'''importing webdriver module from selenium libraray, this module
provides a way to interact with web browers programmatically.'''

from selenium import webdriver

# you can replace chrome with the brower of your choice e.g edge
from selenium.webdriver.chrome.service import Service

'''The By class in Selenium is used to locate elements on a web page. 
It is part of the Selenium WebDriver library and provides a set of mechanisms to 
locate elements using different criteria.Can be used with most browers.'''
from selenium.webdriver.common.by import By
#this will help to press enter when send_keys is used.
from selenium.webdriver.common.keys import Keys
#this will help to wait for content to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''for edge there will be a extra line of code
from msedge.selenium_tools import Edge, EdgeOptions
edge class represents ms webdriver
EdgeOptions class is used for configuring behaviour of Edge Webdriver.'''
search = input("Enter something to search:")

'''Service is class responsible for handling web brower's service.
executable_path is different for different browers.
set the path to the executable file of the web driver.'''

service = Service(executable_path ="chromedriver.exe")

'''initializing a new instance of Chrome webDriver and giving it
service which includes path to the ChromeDriver Executable
for other browers this step is similar'''
driver = webdriver.Chrome(service=service)

'''web driver is basically a piece of software which can act
as a real user.'''
driver.get("https://www.google.ca/")

# this will select the given element 
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()#to clear any pre-existing value in the selected element.
#this will type in given string in the variable
input_element.send_keys("amazon"+Keys.ENTER) 

#wait for our target then click on it 
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'd8lRkd'))
)
element.click()
# input_element2 = driver.find_element(By.XPATH,"//span[contains(@class, 'x2VHCd') and contains(@class, 'OSrXXb') and contains(@class, 'ob91vb')]")
# if element.is_displayed() and element.is_enabled():
#     element.click()
#inside amazon
input_element1 = driver.find_element(By.ID,"twotabsearchtextbox")
input_element1.send_keys(search+Keys.ENTER) 
time.sleep(20)#the bot will keep working for 5 seconds then the program will end.
driver.quit()

