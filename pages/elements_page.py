from components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ElementsPage:
    def __init__(self, browser):
        self.browser = browser
        self.center_message = BaseComponent(
            browser,
            (By.CSS_SELECTOR, ".pattern-backdrop + div")
        )

    def wait_for_page_load(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "main-header"))
        )