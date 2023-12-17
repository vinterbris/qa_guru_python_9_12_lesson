import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function')
def setup_browser(request):
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://user1:1234@selenoid:4444/wd/hub",
        desired_capabilities=capabilities)

    yield
    browser.quit()
