from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseComponent:
    def __init__(self, browser, selector):
        self.browser = browser
        self.selector = selector

    def find_element(self):
        wait = WebDriverWait(self.browser, 10)
        return wait.until(EC.presence_of_element_located(self.selector))

    def get_text(self):
        return str(self.find_element().text)