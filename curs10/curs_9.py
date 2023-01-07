import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Test(unittest.TestCase):
    base_url = 'https://www.itfactory.ro/ta-32/'
    password_for_32= 'poZAET6XvBqgUWI'

    def test_open_the_IFpage_for_32(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        driver.maximize_window()
        # sleep(500)
        # driver.implicitly_wait(4)
        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
        password_input = driver.find_element(By.CSS_SELECTOR, 'p input[type="password"]')

        password_input.send_keys(self.password_for_32)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'input[name="Submit"]')
        submit_button.click()

        actual_url = driver.current_url
        trainer_name = driver.find_element(By.CSS_SELECTOR, '.elementor-text-editor > ul > li:nth-child(2) > strong')

        assert actual_url == 'https://www.itfactory.ro/ta-32/', 'You are not on the correct page!'
        assert trainer_name.text.__contains__('Mihai Vaman')
        driver.delete_all_cookies()
        driver.quit()

    def test_check_courses_for_32(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        driver.maximize_window()

        password_input = driver.find_element(By.CSS_SELECTOR, 'p input[type="password"]')
        password_input.send_keys(self.password_for_32)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'input[name="Submit"]')
        submit_button.click()

        # sleep(500)
        ActionChains(driver).move_to_element(
            driver.find_element(By.CSS_SELECTOR, 'div[data-id="5d49f7a6"]')).perform()

        curses_list = driver.find_elements(By.CSS_SELECTOR, '.elementor-element-1e210433 h2')
        print('\n')
        for curse in curses_list:
            print(curse.text)

        assert len(curses_list) == 4


        driver.delete_all_cookies()
        driver.quit()


# class Test(unittest.TestCase):
#     base_url = 'https://www.itfactory.ro/ta-32/'
#     password_for_29 = 'poZAET6XvBqgUWI'
#
#     def test_open_the_IFpage_for_32(self):
#         driver = webdriver.Chrome()
#         driver.get(self.base_url)
#         driver.maximize_window()
#
#         driver.quit()
#
#     def test_open_the_IFpage_for_32_v2(self):
#         driver = webdriver.Chrome()
#         driver.get(self.base_url)
#         driver.maximize_window()
#
#         driver.quit()
#
#     def test_open_the_IFpage_for_32_v3(self):
#         driver = webdriver.Chrome()
#         driver.get(self.base_url)
#         driver.maximize_window()
#
#         driver.quit()
#
#     def test_open_the_IFpage_for_32_v4(self):
#         driver = webdriver.Chrome()
#         driver.get(self.base_url)
#         driver.maximize_window()
#
#         driver.quit()
#
# if __name__ == "__main__":
#     unittest.main