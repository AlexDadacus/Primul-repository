
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
CHROME --------------------------------------------------------------------------
# pentru a rula teste pe Chrome, cu versiunea selenium 4.6.0
driver = webdriver.Chrome()

# pentru a rula teste pe Chrome cu o versiune dinainte de selenium 4.6.0
s = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


FIREFOX --------------------------------------------------------------------------
# pentru a rula teste pe Firefox, cu versiunea selenium 4.6.0
driver = webdriver.Firefox()

# pentru a rula teste pe Firefox cu o versiune dinainte de selenium 4.6.0
s = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=s)

EDGE--------------------------------------------------------------------
# pentru a rula teste pe Edge, cu versiunea selenium 4.6.0
driver = webdriver.Edge()

# pentru a rula teste pe Edge cu o versiune dinainte de selenium 4.6.0 
s = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=s)
"""

driver = webdriver.Firefox()

driver.maximize_window()
driver.get('https://www.google.com')
sleep(6)

first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')
first_name.send_keys('Mihai')

sleep(3)

driver.quit()