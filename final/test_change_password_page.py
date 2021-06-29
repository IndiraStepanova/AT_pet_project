import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.accounts.account_page import AccountPage
from .pages.accounts.change_password_page import ChangePasswordPage
import time

link = "http://selenium1py.pythonanywhere.com/"

password = "!2wsxCDE#"
another_password = "#EDCxsw2!"


@pytest.mark.personal_tests
class TestUserCanChangePassword():
    @pytest.fixture(scope="function", autouse=True)
    # Arrange
    def setup(self, browser):
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        self.login_page.register_new_user(email, password)
        self.account_page = AccountPage(browser, browser.current_url)
        self.account_page.open()
        self.account_page.go_to_account_page()
        self.account_page.go_to_change_password_page()

    
    def test_user_can_change_password_and_save_changes(self, browser):
        account_page = AccountPage(browser, link)
        account_page.open()
        account_page.go_to_account_page()
        account_page.go_to_change_password_page()
        change_password_page = AccountPage(browser, browser.current_url)
        change_password_page.change_password_and_save(
            old_password=password, new_password=another_password)
        change_password_page.should_be_success_message()

    
    def test_user_can_change_password_and_save_changes(self, browser):
        account_page = AccountPage(browser, link)
        account_page.open()
        account_page.go_to_account_page()
        account_page.go_to_change_password_page()
        change_password_page = AccountPage(browser, browser.current_url)
        change_password_page.change_password_and_cancel_of_action(
            old_password=password, new_password=another_password)
        change_password_page.should_not_be_success_message()
