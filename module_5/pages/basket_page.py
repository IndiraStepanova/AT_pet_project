from .base_page import BasePage
from .locators import BasketPageLocators

expected_basket_page_header = {
    "ru": "Корзина",
    "en-gb": "Basket", 
    "fr": "Panier",
    "es": "Carrito"
}

expected_empty_basket_message = {
    "ru": "Ваша корзина пуста",
    "en-gb": "Your basket is empty", 
    "fr": "Votre panier est vide",
    "es": "Tu carrito esta vacío"
}

class BasketPage(BasePage):
    def should_be_basket_page(self, language):
        self.should_be_basket_url()
        self.should_be_basket_header(language)
        self.should_be_empty_basket_form()
        self.should_be_empty_basket_message(language)
    
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "It is not basket URL!"

    def should_be_basket_header(self, language):
        basket_header = self.get_element_text(*BasketPageLocators.BASKET_PAGE_HEADER)
        print("\nbasket header: " + self.get_element_text(*BasketPageLocators.BASKET_PAGE_HEADER))
        assert basket_header in expected_basket_page_header[language], "Basket page header does not match to locale!"
    
    def should_be_empty_basket_form(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_FORM), \
            "Basket form is presented but should not be!"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL_SUM), \
            "Total sum form is presented but should not be!"

    def should_be_empty_basket_message(self, language):
        empty_basket_message = self.get_element_text(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        print("\nbasket messages: " + self.get_element_text(*BasketPageLocators.EMPTY_BASKET_MESSAGE))
        assert expected_empty_basket_message[language] in empty_basket_message, "There is not empty basket message!"




