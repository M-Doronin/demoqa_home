import pytest
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

class TestCheckText:
    def test_footer_text(self, browser):
        demo_qa_page = DemoQa(browser)

        demo_qa_page.visit()

        footer_text = demo_qa_page.footer.get_text()
        expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

        assert footer_text == expected_text, (
            f"Текст в подвале не соответствует ожидаемому. "
            f"Ожидалось: '{expected_text}', получено: '{footer_text}'"
        )

    def test_center_text_on_elements_page(self, browser):
        demo_qa_page = DemoQa(browser)
        elements_page = ElementsPage(browser)

        demo_qa_page.visit()

        demo_qa_page.click_elements_button()
        elements_page.wait_for_page_load()

        center_text = elements_page.center_message.get_text()
        expected_text = 'Please select an item from left to start practice.'

        assert center_text == expected_text, (
            f"Центральный текст не соответствует ожидаемому. "
            f"Ожидалось: '{expected_text}', получено: '{center_text}'"
        )