'''
Регистрация нового пользователя:
1. войти на сайт http://selenium1py.pythonanywhere.com/
2. перейти в модуль авторизации/ регистрации
3. фокус на блок регистрации
4. ввод логина (+)
5. ввод пароля (+)
6. войти в лк
7. проверить, что еmail пользователя соответствует указанному при регистрации

Авторизация ранее зарегистрированного пользователя (+):
1. войти на сайт http://selenium1py.pythonanywhere.com/
2. перейти в модуль авторизации/ регистрации
3. фокус на блок авторизации
4. ввод логина (+)
5. ввод пароля (+)
6. войти в ЛК
7. проверить, что еmail пользователя соответствует указанному при регистрации

Авторизация ранее зарегистрованного пользователя (-):
1. войти на сайт http://selenium1py.pythonanywhere.com/
2. перейти в модуль авторизации/ регистрации
3. фокус на блок авторизации
4. ввод логина (+) (-) (-)
5. ввод пароля (-) (+) (-)
6. пользователь НЕ авторизован
7. возникает сообщение об ошибке авторизации

Удаление учетной записи пользователя:
1. Авторизоваться на сайте
2. Войти в ЛК
3. Нажать "Удалить учетную запись"
4. Ввести пароль пользователя
5. Подтвердить удаление УЗ
6. учетная запись удалена, о чем говорит соответствующее сообщение
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

#Common:
main_page_link = "http://selenium1py.pythonanywhere.com/"
search_redirect_to_login_link = "#login_link"
search_account_link_locator = ".collapse > div > ul > li:nth-child(1) > a"
search_profile_locator = "div > table > tbody :nth-child(2) > td"

#Locators for registration:
search_reg_email_locator = "#id_registration-email"
search_reg_password_locator = "#id_registration-password1"
search_reg_repeat_password_locator = "#id_registration-password2"
search_reg_button_locator = "[name = 'registration_submit']"

#Locators for auth:
search_redirect_to_login_link = "#login_link"
search_auth_email_locator = "#id_login-username"
search_auth_password_locator = "#id_login-password"
search_auth_button_locator = "[name = 'login_submit']"
#Locators for neg tests:
search_alert_danger_locator = ".alert.alert-danger strong"

#Locators for delete:
search_delete_button_locator = "#delete_profile"
search_password_for_delete_account_locator = "input#id_password"
search_submit_delete_profile = ".btn.btn-lg.btn-danger"
search_profile_delete_message_locator = ".alertinner.wicon"

# Data:
user_email = "IIvanov@email.com"
user_password = "!2wsxCDE#"

def open_browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(main_page_link)
    browser.find_element_by_css_selector(search_redirect_to_login_link).click()
    return browser

def check_reg_user(browser):
    input_user_email = browser.find_element_by_css_selector(search_reg_email_locator)
    input_user_email.send_keys(user_email) 
    input_user_password = browser.find_element_by_css_selector(search_reg_password_locator)
    input_user_password.send_keys(user_password)
    repeat_user_password = browser.find_element_by_css_selector(search_reg_repeat_password_locator)
    repeat_user_password.send_keys(user_password)
    browser.find_element_by_css_selector(search_reg_button_locator).click()

def check_auth_user(browser, us_name, us_pass):
    input_user_email = browser.find_element_by_css_selector(search_auth_email_locator)
    input_user_email.send_keys(us_name)
    input_user_password = browser.find_element_by_css_selector(search_auth_password_locator)
    input_user_password.send_keys(us_pass)
    browser.find_element_by_css_selector(search_auth_button_locator).click()


def test_reg_user():
    try:
        # Arrange
        browser = open_browser()
        # Act
        check_reg_user(browser)
        #Assert
        browser.find_element_by_css_selector(search_account_link_locator).click()
        user_logged = browser.find_element_by_css_selector(search_profile_locator)
        assert user_email in user_logged.text, "Email пользователя не соответствует указанному в учетной записи!"

    finally:
        browser.quit()

def test_auth_user_negativ():
    try:
        # Arrange
        browser = open_browser()
        # Act
        check_auth_user(browser, "not_existed@mail.tu", "123")
        #Assert
        user_not_logged = browser.find_element_by_css_selector(search_alert_danger_locator)
        WebDriverWait(browser, 5).until(EC.visibility_of(user_not_logged))
        #проверяем, что при вводе неверного логина/ пароля возникает ошибка авторизации
        assert "Опаньки!" in user_not_logged.text, "Пользователь вошел на сайт не со своими учетными данными, дубина!"
    finally:
        browser.quit()

def test_auth_user_positiv():
    try:
        # Arrange
        browser = open_browser()
        # Act
        check_auth_user(browser, user_email, user_password)
        
        browser.find_element_by_css_selector(search_account_link_locator).click()
        #Assert
        user_logged = browser.find_element_by_css_selector(search_profile_locator)
        assert user_email in user_logged.text, "Введеный при авторизации логин не соответствует логину пользователя!"
    finally:
        browser.quit()

def test_user_delete():
    try:
        #Arrange
        browser = open_browser()
        check_auth_user(browser, user_email, user_password)
        browser.find_element_by_css_selector(search_account_link_locator).click()
        #Act
        delete_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_delete_button_locator)))
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


test_reg_user()
test_auth_user_negativ() 
test_auth_user_positiv()
test_user_delete()
