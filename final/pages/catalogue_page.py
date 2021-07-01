from .base_page import BasePage
from .locators import CataloguePageLocators


class CataloguePage(BasePage):
    def should_be_guest_can_add_goods_to_basket(self):
        add_first_goods_in_page = self.browser.find_element(
            *CataloguePageLocators.ADD_TO_BASKET_FROM_COMMON_PAGE)
        add_first_goods_in_page.click()

    def sum_of_basket_must_be_equal_to_the_price_of_goods(self):
        price_of_goods = self.get_element_text(
            *CataloguePageLocators.PRICE_OF_GOODS)
        sum_of_basket = self.get_element_text(
            *CataloguePageLocators.PRICE_OF_GOODS)
        assert price_of_goods == sum_of_basket, "Sum of the basket does not equal to the price of goods!"

    def should_be_success_message(self):
        assert self.is_element_present(*CataloguePageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CataloguePageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be!"
