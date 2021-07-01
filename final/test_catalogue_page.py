import pytest
from .pages.login_page import LoginPage
from .pages.catalogue_page import CataloguePage
from .pages.accounts.account_page import AccountPage
import time

link = "https://selenium1py.pythonanywhere.com/ru/catalogue/"

password = "!2wsxCDE#"
another_password = "#EDCxsw2!"


@pytest.mark.personal_tests
class TestCataloguePage():
    def test_guest_can_add_goods_to_basket(self, browser):
        # Arrange
        page = CataloguePage(browser, link)
        page.open()
        # Act
        page.should_be_guest_can_add_goods_to_basket()
        # Assert
        page.should_be_success_message()
        page.sum_of_basket_must_be_equal_to_the_price_of_goods()

    def test_guest_can_go_to_login_page_from_catalogue_page(self, browser):
        # Arrange
        page = CataloguePage(browser, link)
        page.open()
        page.go_to_login_page()
        # Act
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, password)
        # Assert
        login_page.should_be_authorized_user()
