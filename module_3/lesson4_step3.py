import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number_1 = browser.find_element_by_id("num1")
    number_1_int = number_1.text
    number_2 = browser.find_element_by_id("num2")
    number_2_int = number_2.text
    sum_of_elem = int(number_1_int) + int(number_2_int)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum_of_elem))

    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()
finally:
    time.sleep(5)
    browser.quit()




    
'''
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

'''