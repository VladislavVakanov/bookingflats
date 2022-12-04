import time

from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, *web_element, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((web_element)))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def send_keys(self, *web_element, keys):
        self.browser.find_element(*web_element).send_keys(keys)

    def click(self, *web_element, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((web_element)),
                                                       message='No element on the page!').click()
        except StaleElementReferenceException:
            pass

    def wait_page_loaded(self, timeout=60, check_js_complete=True, check_page_changes=False,
                         wait_for_element=None, wait_for_xpath_to_disappear='', sleep_time=2):

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        source = ''
        try:
            source = self.browser.page_source
        except Exception:
            pass

        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                try:
                    self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self.browser.execute_script('return document.readyState == "complete";')
                except Exception:
                    pass

            if page_loaded and check_page_changes:
                new_source = ''
                try:
                    new_source = self.browser.page_source
                except Exception:
                    pass

                page_loaded = new_source == source
                source = new_source

            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self.browser, 0.1).until(EC.presence_of_element_located(
                        (By.XPATH, wait_for_xpath_to_disappear)))
                except Exception:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self.browser, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element))
                except Exception:
                    pass  # Ignore timeout errors

            assert k < timeout, f'The page loaded more than {timeout} seconds!'

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        self.browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
