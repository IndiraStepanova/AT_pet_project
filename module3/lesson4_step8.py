import math
import time
import os 
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Ivanov")
    email = browser.find_element_by_name("email")
    email.send_keys("IIvanov@email.com")
    attachment = browser.find_element_by_css_selector("input#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file_for_step8.txt')           # добавляем к этому пути имя файла 
    attachment.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
finally:
    time.sleep(5)
    browser.quit()


