from os import times
import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/"

promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestMainPage:
    """ def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
            

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link() """

    def test_guest_can_add_product_to_basket(self, browser, language):
        promo_page = ProductPage(browser, promo_link)
        promo_page.open()
        promo_page.should_be_add_product_to_basket(language)
        promo_page.solve_quiz_and_get_code()
        promo_page.compare_selected_and_added_product()
        
   