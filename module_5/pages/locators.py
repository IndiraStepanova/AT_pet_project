from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    #Locators for auth:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name = 'login_submit']")
    #Locators for registration:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_page .product_main h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_page .product_main .price_color")
    PRODUCT_ADDED_ALLERT_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_PRICE_ALLERT_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
