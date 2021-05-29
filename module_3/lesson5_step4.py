import math
import time
from selenium import webdriver


link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
    #работа с модальным окном:
    confirm = browser.switch_to.alert
    confirm.accept()
    #найти х и посчитать функцию от Х:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    for_answer = browser.find_element_by_id("answer")
    for_answer.send_keys(calc(x))
    #submit в новом окне:
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
