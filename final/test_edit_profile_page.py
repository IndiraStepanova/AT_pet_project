from final.pages.accounts.edit_profile_page import EditProfilePage
import pytest
from .pages.login_page import LoginPage
from .pages.accounts.account_page import AccountPage
from .pages.accounts.change_password_page import ChangePasswordPage
import time

link = "http://selenium1py.pythonanywhere.com/"

password = "!2wsxCDE#"
another_password = "#EDCxsw2!"


@pytest.mark.draft_of_tests
class TestUserCanChangePassword():
    @pytest.fixture(scope="function", autouse=True)
    # Arrange
    def setup(self, browser):
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        self.login_page.register_new_user(email, password)
        self.login_page.go_to_account_page()
        self.account_page = AccountPage(browser, browser.current_url)
        self.account_page.open()
        self.account_page.go_to_edit_profile_page()

    def test_user_can_edit_profile_and_save_changes(self, browser):
        assert True

    def test_user_can_edit_profile_and_cancel_changes(self, browser):
        assert True
