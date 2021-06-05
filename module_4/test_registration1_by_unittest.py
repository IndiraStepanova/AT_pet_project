
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TestRegistration(unittest.TestCase):
    
    
    def test_registration_first(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        #Заполняем обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector(".first_block .form-control.second")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_css_selector(".first_block .form-control.third")
        email.send_keys("email@email.com")
        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        WebDriverWait(browser, 2).until(EC.visibility_of(welcome_text_elt))
        assert welcome_text_elt.text == "Congratulations! You have successfully registered!", "Registration failed!"
    
    def test_registration_another(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        #Заполняем обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector(".first_block .form-control.second")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_css_selector(".first_block .form-control.third")
        email.send_keys("email@email.com")
        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        WebDriverWait(browser, 2).until(EC.visibility_of(welcome_text_elt))
        assert welcome_text_elt.text == "Congratulations! You have successfully registered!", "Registration failed!"
        

if __name__ == '__main__':
    unittest.main()