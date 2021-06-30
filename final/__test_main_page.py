import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        page.open()
        # Assert
        page.should_be_login_link()


@pytest.mark.success_messages_absent
class TestAddToBasketMessages():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, language):
        # Arrange
        promo_page = ProductPage(browser, promo_link)
        promo_page.open()
        # Act
        promo_page.add_product_to_basket()
        # Assert
        promo_page.should_be_add_to_basket_button(language)
        # убедиться, что сообщения об успехе не появляется на странице в течение заданного времени:
        promo_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, language):
        # Arrange
        promo_page = ProductPage(browser, promo_link)
        # Act
        promo_page.open()
        # Assert
        # убедиться, что сообщения об успехе не появляется на странице в течение заданного времени:
        promo_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, language):
        # Arrange
        promo_page = ProductPage(browser, promo_link)
        promo_page.open()
        # Act
        promo_page.add_product_to_basket()
        # Assert
        promo_page.should_be_add_to_basket_button(language)
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared:
        # убедиться, что элемент исчезает в заданный timeout
        promo_page.should_be_success_message_is_disappeared()


class TestMainPage():
    @pytest.mark.parametrize('promo_offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                             pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, language, promo_offer):
        # Arrange
        promo_page = ProductPage(browser, promo_link+f"/?promo={promo_offer}")
        promo_page.open()
        # Act
        promo_page.add_product_to_basket()
        promo_page.solve_quiz_and_get_code()
        # Assert
        promo_page.compare_selected_and_added_product()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, language):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_be_empty_basket_page(language)
