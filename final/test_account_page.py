import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.accounts.account_page import AccountPage
from .pages.accounts.change_password_page import ChangePasswordPage
import time

link = "http://selenium1py.pythonanywhere.com/"

password = "!2wsxCDE#"
another_password = "#EDCxsw2!"

# Assert
# self.login_page.should_be_authorized_user()


def test_user_can_open_account_page(self, browser, language):

    # .account_page.should_be_account_page(language)


def test_user_can_go_to_change_password_page(self, browser):
    # self.account_page.go_to_change_password_page()
    change_password_page = AccountPage(browser, browser.current_url)
    change_password_page.should_be_change_password_url()


'''






'''
