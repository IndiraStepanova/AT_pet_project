from .base_page import BasePage
from .locators import ProductPageLocators

#dict for add to basket button
expected_button_text = {
    "ru": "Добавить в корзину",
    "en-gb": "Add to basket", 
    "fr": "Ajouter au panier",
    "es": "Añadir al carrito"
}

class ProductPage(BasePage):
    def should_be_add_product_to_basket(self, language):
        self.should_be_add_to_basket_button(language)
        self.add_product_to_basket()

    def compare_selected_and_added_product(self):
        self.compare_selected_product_name_and_added_product_name()
        self.compare_selected_product_price_and_added_product_price()

    def should_be_add_to_basket_button(self, language):
        button_text = self.get_element_text(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        print("\ntext of button: "+button_text)
        assert button_text in expected_button_text[language], "Incorrect text of button!"
        print("\npress the button...")
        assert self.is_element_clicable(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button is not available!"
    
    def add_product_to_basket(self):
        self.click_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
    
    def compare_selected_product_name_and_added_product_name(self):
        product_added_allert = self.get_element_text(*ProductPageLocators.PRODUCT_ADDED_ALLERT_MESSAGE)
        product_name = self.get_element_text(*ProductPageLocators.NAME_OF_PRODUCT)
        assert product_name == product_added_allert, "Selected and added product name do not match!"
    
    def compare_selected_product_price_and_added_product_price(self):
        product_price_allert = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_ALLERT_MESSAGE)
        product_price = self.get_element_text(*ProductPageLocators.PRICE_OF_PRODUCT)
        assert product_price == product_price_allert, "Selected and added product price do not match!"
        


        