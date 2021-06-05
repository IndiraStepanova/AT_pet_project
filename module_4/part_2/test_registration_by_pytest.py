#Common:
main_page_link = "http://selenium1py.pythonanywhere.com/"
search_redirect_to_login_link = "#login_link"
search_account_link_locator = ".collapse > div > ul > li:nth-child(1) > a"
search_profile_locator = "div > table > tbody :nth-child(2) > td"

#Locators for registration:
search_reg_email_locator = "#id_registration-email"
search_reg_password_locator = "#id_registration-password1"
search_reg_repeat_password_locator = "#id_registration-password2"
search_reg_submit_button_locator = "[name = 'registration_submit']"

# Data:
user_email = "IIvanov@email.com"
user_password = "!2wsxCDE#"

def check_reg_user(browser, email_var, pass_var):
    input_user_email = browser.find_element_by_css_selector(search_reg_email_locator)
    input_user_email.send_keys(email_var) 
    input_user_password = browser.find_element_by_css_selector(search_reg_password_locator)
    input_user_password.send_keys(pass_var)
    repeat_user_password = browser.find_element_by_css_selector(search_reg_repeat_password_locator)
    repeat_user_password.send_keys(pass_var)
    browser.find_element_by_css_selector(search_reg_submit_button_locator).click()

def test_registration_first(browser):
    #Arange
    browser.find_element_by_css_selector(search_redirect_to_login_link).click()
    # Act
    check_reg_user(browser, user_email, user_password)
    browser.find_element_by_css_selector(search_account_link_locator).click()
    #Assert
    user_logged = browser.find_element_by_css_selector(search_profile_locator)
    assert user_email in user_logged.text, "The user's email address does not match the one specified in the account!"