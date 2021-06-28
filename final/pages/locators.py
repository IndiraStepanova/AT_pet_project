from selenium.webdriver.common.by import By

class AccountPageLocators():
    ACCOUNT_PAGE_HEADER = (By.CSS_SELECTOR, ".page-header.action h1")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".page_inner .row a:nth-child(5)")
    EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, ".page_inner .row a:nth-child(6)")
    DELETE_PROFILE_BUTTON = (By.CSS_SELECTOR, ".page_inner .row a:nth-child(7)")
    
    #Locators for change password
    OLD_PASSWORD = (By.CSS_SELECTOR, "#id_old_password")
    NEW_PASSWORD = (By.CSS_SELECTOR, "#id_new_password1")
    NEW_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_new_password2")
    CHANGE_PASSWORD_SUBMIT = (By.CSS_SELECTOR, "#change_password_form [type = 'submit']")
    CHANGE_PASSWORD_CANCEL = (By.CSS_SELECTOR, "#change_password_form > div:nth-child(5) a")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
    #Locators for edit profile
    #Locators for delete profile

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    ACCOUNT_LINK = (By.CSS_SELECTOR, ".navbar-right >li:nth-child(1) > a")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # Locators for auth:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name = 'login_submit']")
    # Locators for registration:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT_FIELD = (
        By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (
        By.CSS_SELECTOR, "[name = 'registration_submit']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_page .product_main h1")
    PRICE_OF_PRODUCT = (
        By.CSS_SELECTOR, ".product_page .product_main .price_color")
    PRODUCT_ADDED_ALLERT_MESSAGE = (
        By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_PRICE_ALLERT_MESSAGE = (
        By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR,
                   ".basket-mini :nth-child(1).btn.btn-default")
    BASKET_PAGE_HEADER = (By.CSS_SELECTOR, ".page-header.action h1")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//*[@id='content_inner']/p")
    BASKET_SUMMARY_FORM = (By.CSS_SELECTOR, ".basket_summary#basket_formset")
    BASKET_TOTAL_SUM = (By.CSS_SELECTOR, "#basket_totals")
