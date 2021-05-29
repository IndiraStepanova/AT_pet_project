import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
browser.get(link)
try:
    book_btn = browser.find_element_by_css_selector("button#book")
    book_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), "$100")
    )
    book_btn.click()

    #вычисляем функцию
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    for_answer = browser.find_element_by_id("answer")
    for_answer.send_keys(calc(x))
    #submit:
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
