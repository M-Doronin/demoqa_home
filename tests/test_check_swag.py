from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    demo_page = SwagLabs(browser)
    demo_page.visit()
    assert demo_page.exist_icon(), "Иконка не найдена на странице"

def test_check_username_field(browser):
    demo_page = SwagLabs(browser)
    demo_page.visit()
    assert demo_page.exist_username_field(), "Поле имени пользователя не найдено"

def test_check_password_field(browser):
    demo_page = SwagLabs(browser)
    demo_page.visit()
    assert demo_page.exist_password_field(), "Поле пароля не найдено"