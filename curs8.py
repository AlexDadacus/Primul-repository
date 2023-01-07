import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# webdriver = webdriver.Chrome()
# webdriver.get('https://www.booking.com')
# site_rezervari = webdriver.find_element(By.CSS_SELECTOR, 'form[method="GET"] button[type="submit"]')
# site_rezervari.click()
# time.sleep(5)

# pas 1
# in terminal punem: pip install webdriver-manager si selenium
# pas 2
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# pas 3
# Seteaza driverul

driver = webdriver.Chrome()

# Navigam catre un url
driver.get('https://phptravels.net/login')
# Selector by ID
password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
login_btn = driver.find_element(By.CSS_SELECTOR, '.btn-box > button[type="submit"]')

password_input.send_keys("ceva")
login_btn.click()

time.sleep(50)
