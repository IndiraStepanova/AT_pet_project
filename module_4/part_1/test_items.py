from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

search_login_link_locator = "#login_link"
search_redirect_link_locator = "li > ul > li:nth-child(1) > a"
search_good_locator = "a[title='Coders at Work']"
search_add_to_basket_locator = "button.btn-add-to-basket"

browser = None

def test_guest_should_see_login_link(browser):
    browser.find_element_by_css_selector(search_redirect_link_locator).click()
    browser.find_element_by_css_selector(search_good_locator).click()
    assert EC.element_to_be_clickable((By.CSS_SELECTOR, search_add_to_basket_locator)), "Button is not available!"
    assert EC.text_to_be_present_in_element(search_add_to_basket_locator, "Добавить в корзину" or "Add to basket" or
                                            "Ajouter au panier" or "Añadir al carrito"), "Incorrect text!"
    
