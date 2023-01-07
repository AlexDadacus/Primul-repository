import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
username = driver.find_element(By.ID, 'username')             # By.ID
username.send_keys('tomsmith')
# ------------------
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
password = driver.find_element(By.ID, 'password')             # By.ID
password.send_keys('SuperSecretPassword!')
time.sleep(10)
# ------------------
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
footer = driver.find_element(By.ID, 'page-footer')             # By.ID
print(footer.get_attribute("outerHTML"))
# ------------------
driver = webdriver.Chrome()
driver.get('http://www.seleniumframework.com/Practiceform/')
driver.find_element(By.LINK_TEXT, 'This is a link').click()                     # By.LINK_TEXT
time.sleep(10)
driver.find_element(By.LINK_TEXT, 'Add Extensions').click()                     # By.LINK_TEXT
time.sleep(10)
driver.find_element(By.LINK_TEXT, 'Setup First Project').click()                # By.LINK_TEXT
time.sleep(10)
# -----------------
driver = webdriver.Chrome()
driver.get('http://www.seleniumframework.com/Practiceform/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Setup Visual').click()               # By.PARTIAL_LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, 'Commands').click()                   # By.PARTIAL_LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, 'Strategies').click()                 # By.PARTIAL_LINK_TEXT
# -----------------
driver = webdriver.Chrome()
driver.get('http://www.seleniumframework.com/Practiceform/')
driver.find_element(By.NAME, 'company').send_keys('Serele SRL')               # By.NAME
time.sleep(10)
driver.find_element(By.NAME, 'name').send_keys('Alex')                        # By.NAME
time.sleep(10)
driver.find_element(By.NAME, 'email').send_keys('dadacusalexandru@yahoo.com')  # By.NAME
time.sleep(10)
# -----------------
driver = webdriver.Chrome()
driver.get('http://www.seleniumframework.com/Practiceform/')
tag1 = driver.find_element(By.TAG_NAME, 'h4')                               # By.TAG_NAME
print(tag1.get_attribute("outerHTML"))
tag2 = driver.find_element(By.TAG_NAME, 'p')                                # By.TAG_NAME
print(tag2.get_attribute("outerHTML"))
tag3 = driver.find_element(By.TAG_NAME, 'h5')                               # By.TAG_NAME
print(tag3.get_attribute("outerHTML"))

# -----------------
driver = webdriver.Chrome()
driver.get('https://www.ebay.com/')
clasa1 = driver.find_element(By.CLASS_NAME, 'hl-cat-nav__expander')
print(clasa1.get_attribute("outerHTML"))                                       # By.CLASS_NAME
driver.get('https://www.ebay.com/')
clasa2 = driver.find_element(By.CLASS_NAME, 'gh-menu')
print(clasa2.get_attribute("outerHTML"))                                       # By.CLASS_NAME
driver.get('https://the-internet.herokuapp.com/login')
clasa3 = driver.find_element(By.CLASS_NAME, 'row')                             # By.CLASS_NAME
print(clasa3.get_attribute("outerHTML"))
# -----------------
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
buton_login = driver.find_element(By.XPATH, '//*[@id="login"]/button')        # By.XPATH
buton_login.click()
time.sleep(10)
driver.get('https://the-internet.herokuapp.com/login')
buton_logout = driver.find_element(By.XPATH, '//*[@id="content"]/div/a/i')    # By.XPATH
buton_logout.click()
time.sleep(10)
driver.get('http://www.seleniumframework.com/Practiceform/')
link_text = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/div/div/a')    # By.XPATH
link_text.click()
time.sleep(10)
