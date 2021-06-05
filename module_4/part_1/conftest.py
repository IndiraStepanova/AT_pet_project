import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                 help="Choose language: ru, en-GB, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "ru":
        print("\nstart ru url for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://selenium1py.pythonanywhere.com/ru/")
    elif language == "en-GB":
        print("\nstart en-gb url for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://selenium1py.pythonanywhere.com/en-gb/")
    elif language == "es":
        print("\nstart es url for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://selenium1py.pythonanywhere.com/es/")
    elif language == "fr":
        print("\nstart fr url for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://selenium1py.pythonanywhere.com/fr/")
    else:
        raise pytest.UsageError("--language should be ru, en-GB, es, fr")
    yield browser
    print("\nquit browser..")
    browser.quit()