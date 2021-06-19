import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import time

link = "http://selenium1py.pythonanywhere.com/"

promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
            

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

class TestMainPage:
    """

    @pytest.mark.parametrize('promo_offer', ["offer0","offer1","offer2","offer3","offer4","offer5","offer6", pytest.param("offer7", marks=pytest.mark.xfail),"offer8","offer9"])
    def test_guest_can_add_product_to_basket(self, browser, language, promo_offer):
        promo_page = ProductPage(browser, promo_link+f"/?promo={promo_offer}")
        promo_page.open()
        promo_page.should_be_add_product_to_basket(language)
        promo_page.solve_quiz_and_get_code()
        promo_page.compare_selected_and_added_product()
     
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, language):
        promo_page = ProductPage(browser, promo_link)
        promo_page.open()
        promo_page.should_be_add_product_to_basket(language)
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present:
        promo_page.should_not_be_success_message(language)
        
    def test_guest_cant_see_success_message(self, browser, language):
        promo_page = ProductPage(browser, promo_link)
        promo_page.open() 
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present:
        promo_page.should_not_be_success_message(language)

    def test_message_disappeared_after_adding_product_to_basket(self, browser, language):
        promo_page = ProductPage(browser, promo_link)
        promo_page.open()
        promo_page.should_be_add_product_to_basket(language)
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared:
        promo_page.should_be_success_message_is_disappeared(language) """
    
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, language):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page(language)
        
    
    
        
        
        
   