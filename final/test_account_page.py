from final.pages.basket_page import BasketPage
from final.pages.accounts.delete_profile import DeleteProfilePage
from final.pages.accounts.edit_profile_page import EditProfilePage
import pytest
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.accounts.account_page import AccountPage
from .pages.accounts.change_password_page import ChangePasswordPage
import time

link = "http://selenium1py.pythonanywhere.com/"

password = "!2wsxCDE#"
another_password = "#EDCxsw2!"


# @pytest.mark.personal_tests
class TestUserCanOpenAccountPage():
    @pytest.fixture(scope="function", autouse=True)
    # Arrange
    def setup(self, browser):
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        self.login_page.register_new_user(email, password)
        self.login_page.go_to_account_page()

    def test_user_can_open_account_page(self, browser, language):
        # Act
        account_page = AccountPage(browser, browser.current_url)
        account_page.open()
        # Assert
        account_page.should_be_main_account_page(language)

# @pytest.mark.personal_tests
class TestAccountPage():
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

    def test_user_can_go_to_change_password_page(self, browser, language):
        # Act
        self.account_page.go_to_change_password_page()
        change_password_page = ChangePasswordPage(browser, browser.current_url)
        change_password_page.open()
        # Assert
        change_password_page.should_be_change_password_page_url()
        change_password_page.should_be_change_password_page_header(language)
    
    def test_user_can_go_to_edit_profile_page(self, browser, language):
        # Act
        self.account_page.go_to_edit_profile_page()
        edit_profile_page = EditProfilePage(browser, browser.current_url)
        edit_profile_page.open()
        # Assert
        edit_profile_page.should_be_edit_profile_page_url()
        edit_profile_page.should_be_edit_profile_page_header(language)

    def test_user_can_go_to_delete_profile_page(self, browser, language):
        # Act
        self.account_page.go_to_delete_profile_page()
        delete_profile_page = DeleteProfilePage(browser, browser.current_url)
        delete_profile_page.open()
        # Assert
        delete_profile_page.should_be_delete_profile_page_url()
        delete_profile_page.should_be_delete_profile_page_header(language)

    def test_user_can_go_to_basket_from_account_page(self, browser, language):
        #Act
        self.account_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        #Assert
        basket_page.should_be_basket_url()
        basket_page.should_be_basket_header(language)
        
    def test_user_can_logout(self, browser):
        # Act
        self.account_page.go_to_logout_link()
        #Assert
        self.account_page.should_be_unauthorized_user()
