'''
Пользовательский сценарий 1.1. Регистрация нового пользователя
Тестовый сценарий 1.1.1. Регистрация нового пользователя
Предусловия: открыта страница регистрации/авторизации http://selenium1py.pythonanywhere.com/ru/accounts/login/
1. В блоке "Зарегистрироваться" ввод в поле "Адрес электронной почты" адреса электронной почты
2. Ввод и подтверждение пароля удовлетворяющего требованиям
3. Нажать кнопку "Зарегистрироваться"

Ожидаемый результат:
1. Поля ввода активны
2. Регистрация произведена
3. На указанный адрес электронной почты пришла ссылка для подтверждения регистрации
'''

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/"

search_redirect_to_login_link = "#login_link"
search_email_locator = "#id_registration-email"
search_password_locator = "#id_registration-password1"
search_rep_password_locator = "#id_registration-password2"
search_button_locator = "[name = 'registration_submit']"
search_account_link_locator = ".collapse > div > ul > li:nth-child(1) > a"
search_profile_locator = "div > table > tbody :nth-child(2) > td"

def test_login_of_new_user():
    #Data
    user_email = "IIvanov@email.com"
    user_password = "!2wsxCDE#"


    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        search_input = browser.find_element_by_css_selector(search_redirect_to_login_link).click()
        
        # Act
        input_user_email = browser.find_element_by_css_selector(search_email_locator)
        input_user_email.send_keys(user_email) 
        input_user_password = browser.find_element_by_css_selector(search_password_locator)
        input_user_password.send_keys(user_password)
        repeat_user_password = browser.find_element_by_css_selector(search_rep_password_locator)
        repeat_user_password.send_keys(user_password)
        browser.find_element_by_css_selector(search_button_locator).click()
        

        # Assert
        browser.find_element_by_css_selector(search_account_link_locator).click()
        user_logged = browser.find_element_by_css_selector(search_profile_locator)
        assert user_email in user_logged.text, "Пользователь не зареган"

    finally:
        browser.quit()

test_login_of_new_user()