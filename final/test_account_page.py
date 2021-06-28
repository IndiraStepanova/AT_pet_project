import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.account_page import AccountPage
import time

link = "http://selenium1py.pythonanywhere.com/"

password = "!2wsxCDE#"
another_password = "#EDCxsw2!"


@pytest.mark.personal_tests
class TestUserCanEditProfile():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #Arrange
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.go_to_login_page()
        #Act
        email = str(time.time()) + "@fakemail.org"
        self.login_page.register_new_user(email, password)
        # Assert
        self.login_page.should_be_authorized_user()

    def test_user_can_open_account_page(self, browser, language):
        account_page = AccountPage(browser, link)
        account_page.open()
        account_page.go_to_account_page()
        account_page.should_be_account_page(language)

    
    def test_user_can_go_to_change_password_page(self, browser):
        account_page = AccountPage(browser, link)
        account_page.open()
        account_page.go_to_account_page()
        account_page.go_to_change_password_page()
        change_password_page = AccountPage(browser, browser.current_url)
        change_password_page.should_be_change_password_url()

    @pytest.mark.skip
    def test_user_can_change_password_and_save_changes(self, browser):
        account_page = AccountPage(browser, link)
        account_page.open()
        account_page.go_to_account_page()
        account_page.go_to_change_password_page()
        change_password_page = AccountPage(browser, browser.current_url)
        change_password_page.change_password_and_save(
            old_password=password, new_password=another_password)
        change_password_page.should_be_success_message()

    @pytest.mark.skip
    def test_user_can_change_password_and_save_changes(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_account_page()
        account_page = AccountPage(browser, browser.current_url)
        account_page.go_to_change_password_page()
        change_password_page = AccountPage(browser, browser.current_url)
        change_password_page.change_password_and_cancel_of_action(
            old_password=password, new_password=another_password)
        change_password_page.should_not_be_success_message()


'''
@pytest.mark.personal_tests
def test_user_can_delete_own_account(self, browser):
        assert True

@pytest.mark.personal_tests
def test_user_can_logout(self, browser):
        assert True

@pytest.mark.personal_tests
def test_user_can_edit_profile_and_save(self, browser):
        assert True

@pytest.mark.personal_tests
def test_user_can_edit_profile_and_cancel(self, browser):
        assert True

@pytest.mark.personal_tests
def test_user_can_change_password_and_save(self, browser):
        assert True

@pytest.mark.personal_tests
def test_user_can_change_password_and_cancel(self, browser):
        assert True
'''
