import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Login(unittest.TestCase):
    base_url = 'https://the-internet.herokuapp.com/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = webdriver.Chrome()
        self.base_url = driver.current_url
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        time.sleep(5)
        self.new_url = driver.current_url

    def tearDown(self):

        self.driver.quit()

    def test_url_corect_Test_1(self):
        # assert self.new_url != self.base_url
        if self.new_url == "https://the-internet.herokuapp.com/login":
            print("The URL is correct.")
        else:
            print("The URL is incorrect.")

    def test_page_title_Test_2(self):
        self.driver.get('https://the-internet.herokuapp.com/login')
        title = self.driver.find_element(By.XPATH, '/html/head/title')
        t1 = title.get_attribute("outerHTML")
        assert t1 == "<title>The Internet</title>"

    def test_element_h2(self):
        self.driver.get('https://the-internet.herokuapp.com/login')
        h2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h2')
        h2prim = h2.get_attribute("outerHTML")
        assert h2prim == "<h2>Login Page</h2>"

