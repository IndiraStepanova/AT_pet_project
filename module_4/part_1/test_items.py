from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#Common
main_page_link = "http://selenium1py.pythonanywhere.com/"
search_login_link_locator = "#login_link"
search_redirect_link_locator = "li > ul > li:nth-child(1) > a"
search_language_of_page = ".no-js"

#Locators of good
search_good_locator = "a[title='Coders at Work']"

#Add to Basket
search_add_to_basket_locator = "button.btn-add-to-basket"

#dict for add to basket button
expected_button_text = {
    "ru": "Добавить в корзину",
    "en-gb": "Add to basket", 
    "fr": "Ajouter au panier",
    "es": "Añadir al carrito"
}

def test_guest_should_see_login_link(browser, language):
    #Arrange
    browser.implicitly_wait(5)
    browser.get(main_page_link)
    #Assert
    browser.find_element_by_css_selector(search_redirect_link_locator).click()
    browser.find_element_by_css_selector(search_good_locator).click()
    add_to_basket = browser.find_element_by_css_selector(search_add_to_basket_locator)
    language_of_page = browser.find_element_by_css_selector(search_language_of_page).get_attribute("lang")
    #Assert
    assert language_of_page == language, "The language of page does not match the locale!"
    assert add_to_basket.text in expected_button_text[language], "Incorrect text!"
    assert EC.element_to_be_clickable((By.CSS_SELECTOR, search_add_to_basket_locator)), "Button is not available!"
    
    
