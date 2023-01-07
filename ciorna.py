import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium import webdriver
#
# # Set up the webdriver
# driver = webdriver.Chrome()
#
# # Navigate to the page you want to test
# driver.get('http://www.example.com')
#
# # Find the element you want to click on
# link = driver.find_element_by_link_text('Click me')
#
# # Get the URL of the page you are currently on
# original_url = driver.current_url
#
# # Click the link
# link.click()
#
# # Get the URL of the page you are now on
# new_url = driver.current_url
#
# # Verify that the URL has changed
# assert new_url != original_url
#
# # You can also use the assert function to verify that the URL is the correct one
# assert new_url == 'http://www.example.com/expected-page'
#
# # Close the webdriver
# driver.quit()
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
h2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/h2')
h2prim = h2.get_attribute("outerHTML")
print(h2prim)
