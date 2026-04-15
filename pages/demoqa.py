from components.base_component import BaseComponent
from selenium.webdriver.common.by import By

class DemoQa:
    def __init__(self, browser):
        self.browser = browser
        self.footer = BaseComponent(browser, (By.CSS_SELECTOR, "footer"))
        self.btn_elements = BaseComponent(
            browser,
            (By.XPATH, "//span[text()='Elements']")
        )

    def visit(self):
        self.browser.get("https://demoqa.com/")

    def click_elements_button(self):
        self.btn_elements.find_element().click()