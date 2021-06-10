import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                 help="Choose language: ru, en-gb, es, fr")
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                 help="Choose browser: chrome or firefox")

@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("browser_name")

@pytest.fixture(scope="function")
def browser(language):
    options=Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language, 'intl.' = browser_name})
    browser=webdriver.Chrome(options=options)
    yield browser
    browser.quit()


