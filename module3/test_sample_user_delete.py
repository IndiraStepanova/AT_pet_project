'''
Авторизация ранее зарегистрированного пользователя
1. войти на сайт http://selenium1py.pythonanywhere.com/
2. перейти в модуль авторизации/ регистрации
3. фокус на блок авторизации
4. ввод логина (+)
5. ввод пароля (+)
6. войти в ЛК
7. удалить учетную запись
8. учетная запись удалена, о чем говорит соответствующее сообщение
'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/"

search_redirect_to_login_link = "#login_link"
search_email_locator = "#id_login-username"
search_password_locator = "#id_login-password"
search_button_locator = "[name = 'login_submit']"
search_account_link_locator = ".collapse > div > ul > li:nth-child(1) > a"
search_profile_locator = "div > table > tbody :nth-child(2) > td"
search_delete_button_locator = "#delete_profile"
search_password_for_delete_account_locator = "input#id_password"
search_submit_delete_profile = ".btn.btn-lg.btn-danger"
search_profile_delete_message_locator = ".alertinner.wicon"

# Data
user_email = "IIvanov@email.com"
user_password = "!2wsxCDE#"

def open_browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(main_page_link)
    browser.find_element_by_css_selector(search_redirect_to_login_link).click()
    return browser

def test_login_user():
    try:
        # Arrange
        browser = open_browser()
        # Act
        input_user_email = browser.find_element_by_css_selector(search_email_locator)
        input_user_email.send_keys(user_email)
        input_user_password = browser.find_element_by_css_selector(search_password_locator)
        input_user_password.send_keys(user_password)
        browser.find_element_by_css_selector(search_button_locator).click()
        browser.find_element_by_css_selector(search_account_link_locator).click()
         # Assert
        user_logged = browser.find_element_by_css_selector(search_profile_locator)
        assert user_email in user_logged.text, "Введеный при авторизации логин не соответствует логину пользователя!"

    finally:
        #time.sleep(30)
        browser.quit()

def test_user_delete():
    try:
        #Arrange
        browser = open_browser()
        test_login_user()
        #Act
        delete_button = WebDriverWait(browser,10).until(EC.######(search_delete_button_locator))
        delete_button.click()
        delete_account = browser.find_element_by_css_selector(search_password_for_delete_account_locator)
        delete_account.send_keys(user_password)
        browser.find_element_by_css_selector(search_submit_delete_profile).click()

        # Assert
        profile_delete_message = browser.find_element_by_css_selector(
        search_profile_delete_message_locator)
        assert "Ваш профиль удален" in profile_delete_message.text, "Пользователь не удален"

    finally:
        browser.quit()

test_login_user()
test_user_delete()
