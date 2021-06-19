import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.login_guest
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestProductPage:
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, language):
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page(language)

class TestUserAddToBasketFromProductPage():
    def test_user_cant_see_success_message(self, browser, language):
        promo_page = ProductPage(browser, link)
        promo_page.open() 
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present:
        promo_page.should_not_be_success_message(language)

    def test_user_can_add_product_to_basket(self, browser, language):
        promo_page = ProductPage(browser, link)
        promo_page.open()
        promo_page.should_be_add_product_to_basket(language)
        promo_page.solve_quiz_and_get_code()
        promo_page.compare_selected_and_added_product()
