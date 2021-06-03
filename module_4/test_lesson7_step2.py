from re import search
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

search_answer_locator = 'textarea[placeholder="Напишите ваш ответ здесь..."]'
search_submit_button_locator = "button.submit-submission"
search_hint_locator = ".smart-hints__hint"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('end_of_link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, end_of_link):
    #Arrange
    link = f"https://stepik.org/lesson/{end_of_link}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    #Act
    input_answer = browser.find_element_by_css_selector(search_answer_locator)
    answer = math.log(int(time.time()))
    input_answer.send_keys(str(answer))
    browser.find_element_by_css_selector(search_submit_button_locator).click()
    #Assert
    hint_message = browser.find_element_by_css_selector(search_hint_locator)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_hint_locator)))
    assert "Correct!" in  hint_message.text, "Текст не соответствует искомому"

    


