search_login_link_locator = "#login_link"
search_redirect_link_locator = "li > ul > li:nth-child(1) > a"
search_good_locator = "a[title='Coders at Work']"
search_add_to_basket_locator = "button.btn-add-to-basket"

browser = None

def test_guest_should_see_login_link(browser):
    browser.find_element_by_css_selector(search_redirect_link_locator).click()
    browser.find_element_by_css_selector(search_good_locator).click()
    browser.find_element_by_css_selector(search_add_to_basket_locator).click()
    
