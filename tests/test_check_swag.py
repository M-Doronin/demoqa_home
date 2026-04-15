import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


import pytest
from pages.swag_labs import SwagLabs

class TestSwagLabs:
    def test_check_icon_presence(self, browser):
        swag_page = SwagLabs(browser)

        swag_page.visit()

        assert swag_page.exist_icon(), "Иконка логотипа не найдена на странице"

    def test_check_username_field_presence(self, browser):
        swag_page = SwagLabs(browser)

        swag_page.visit()

        assert swag_page.exist_username_field(), "Поле имени пользователя не найдено"

    def test_check_password_field_presence(self, browser):
        swag_page = SwagLabs(browser)

        swag_page.visit()

        assert swag_page.exist_password_field(), "Поле пароля не найдено"