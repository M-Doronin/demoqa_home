from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SwagLabs(BasePage):
    def exist_icon(self):
        try:
            self.find_element((By.CSS_SELECTOR, 'div.login_logo'))
            return True
        except NoSuchElementException:
            return False

    def exist_username_field(self):
        try:
            self.find_element((By.ID, 'user-name'))
            return True
        except NoSuchElementException:
            return False

    def exist_password_field(self):
        try:
            self.find_element((By.ID, 'password'))
            return True
        except NoSuchElementException:
            return False