from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def visit(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)