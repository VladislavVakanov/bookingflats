from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest

options = Options()
options.add_argument('--disable-notifications')
options.add_argument('start-maximized')
options.add_argument('--log-level=DEBUG')

@pytest.fixture
def browser():
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1920, 1080)
    browser.delete_all_cookies()
    yield browser
    browser.quit()