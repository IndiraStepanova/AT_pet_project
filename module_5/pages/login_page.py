from module_4.test_lesson7_step2 import browser
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):                
        assert "login" in self.browser.current_url, "It is not login URL!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_FIELD), "Username field is not presented!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Password field is not presented!"
        assert self.is_element_clicable(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), "Submit button is not clicable!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTER_USERNAME_FIELD), "Username field is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD), "Password field is not presented!"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_REPEAT_FIELD), "Password repeat field is not presented!"
        assert self.is_element_clicable(*LoginPageLocators.REGISTER_USERNAME_FIELD), "Submit button is not clicable!"