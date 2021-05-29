import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_element = browser.find_element_by_id("treasure")
    x_element = treasure_element.get_attribute("valuex")
    for_answer = browser.find_element_by_id("answer")
    for_answer.send_keys(calc(x_element))

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()