'''
Авторизация ранее зарегистрированного пользователя
1. войти на сайт http://selenium1py.pythonanywhere.com/
2. перейти в модуль авторизации/ регистрации
3. фокус на блок авторизации
4. ввод логина (+) (-) (-)
5. ввод пароля (-) (+) (-)
6. пользователь НЕ авторизован
7. возникает сообщение об ошибке авторизации
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/"

search_redirect_to_login_link = "#login_link"
search_email_locator = "#id_login-username"
search_password_locator = "#id_login-password"
search_button_locator = "[name = 'login_submit']"
search_alert_danger_locator = ".alert.alert-danger"

def test_negativ_authorization():
    #Data
    user_email = "IIvanov@email.com"
    user_password = "12345678"


    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        browser.find_element_by_css_selector(search_redirect_to_login_link).click()
        
        # Act
        input_user_email = browser.find_element_by_css_selector(search_email_locator)
        input_user_email.send_keys(user_email) 
        input_user_password = browser.find_element_by_css_selector(search_password_locator)
        input_user_password.send_keys(user_password)
        browser.find_element_by_css_selector(search_button_locator).click()
        

        # Assert
        user_not_logged = browser.find_element_by_css_selector(search_alert_danger_locator)
        assert "Опаньки!" in user_not_logged.text, "Пользователь вошел на сайт не со своими учетными данными, дубина!"

    finally:
        browser.quit()

test_negativ_authorization()