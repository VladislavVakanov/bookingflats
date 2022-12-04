import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import BookingPageLocators
from conf import FIO, PHONE_NUMBER, EMAIL

class BookingPage(BasePage):
    def should_be_booking_page(self):
        self.should_be_booking_page_url()

    def should_be_booking_page_url(self):
        assert 'dom-madrid' in self.browser.current_url, 'Current URL does not contains "dom-madrid"'

    def get_all_numbers_of_flats(self):
        get_flats = []
        new_list = []
        ads  = 0
        sa = 0
        while True:
            flats = self.browser.find_elements(*BookingPageLocators.NUMBERS_OF_FLATS)
            sa = ads
            for flat in flats:
                if sa != 0:
                    sa -=1
                    continue
                if len(flat.text) > 3:
                    get_flats.append(flat.text[6:])
                if len(flat.text) < 4:
                    get_flats.append(flat.text)
            ActionChains(self.browser).move_to_element(self.browser.find_element(By.XPATH, '//img[@class=" ls-is-cached lazyloaded"]')).perform()
            self.click(*BookingPageLocators.SHOW_MORE_BUTTON)
            ads +=12
            time.sleep(0.75)
        print(get_flats)

        first_flat = get_flats.index('128') + 1
        second_flat = get_flats.index('136') + 1
        third_flat = get_flats.index('132') + 1
        fourth_flat = get_flats.index('133') + 1
        fifth_flat = get_flats.index('44') + 1

        try:
            self.browser.find_element(By.XPATH,
                                     f'(//td[@style="display: flex;align-items: center;justify-content: center;"])[{first_flat}]').click()
            self.click(*BookingPageLocators.REQUEST_BUTTON)
            self.click(*BookingPageLocators.AGREE_RADIO_BUTTON)
            self.send_keys(*BookingPageLocators.NAME_INPUT, keys=FIO)
            self.send_keys(*BookingPageLocators.NUMBER_INPUT, keys=PHONE_NUMBER)
            self.send_keys(*BookingPageLocators.EMAIL_INPUT, keys=EMAIL)
            self.click(*BookingPageLocators.EXIT_BUTTON)
        except:
            self.click(*BookingPageLocators.IF_FLAT_IS_REQUESTED)

        try:
            self.browser.find_element(By.XPATH,
                                     f'(//td[@style="display: flex;align-items: center;justify-content: center;"])[{second_flat}]').click()
            self.click(*BookingPageLocators.REQUEST_BUTTON)
            self.click(*BookingPageLocators.AGREE_RADIO_BUTTON)
            self.send_keys(*BookingPageLocators.NAME_INPUT, keys=FIO)
            self.send_keys(*BookingPageLocators.NUMBER_INPUT, keys=PHONE_NUMBER)
            self.send_keys(*BookingPageLocators.EMAIL_INPUT, keys=EMAIL)
            self.click(*BookingPageLocators.EXIT_BUTTON)
        except:
            self.click(*BookingPageLocators.IF_FLAT_IS_REQUESTED)

        try:
            self.browser.find_element(By.XPATH,
                                     f'(//td[@style="display: flex;align-items: center;justify-content: center;"])[{third_flat}]').click()
            self.click(*BookingPageLocators.REQUEST_BUTTON)
            self.click(*BookingPageLocators.AGREE_RADIO_BUTTON)
            self.send_keys(*BookingPageLocators.NAME_INPUT, keys=FIO)
            self.send_keys(*BookingPageLocators.NUMBER_INPUT, keys=PHONE_NUMBER)
            self.send_keys(*BookingPageLocators.EMAIL_INPUT, keys=EMAIL)
            self.click(*BookingPageLocators.EXIT_BUTTON)
        except:
            self.click(*BookingPageLocators.IF_FLAT_IS_REQUESTED)

        try:
            self.browser.find_element(By.XPATH,
                                      f'(//td[@style="display: flex;align-items: center;justify-content: center;"])[{fourth_flat}]').click()
            self.click(*BookingPageLocators.REQUEST_BUTTON)
            self.click(*BookingPageLocators.AGREE_RADIO_BUTTON)
            self.send_keys(*BookingPageLocators.NAME_INPUT, keys=FIO)
            self.send_keys(*BookingPageLocators.NUMBER_INPUT, keys=PHONE_NUMBER)
            self.send_keys(*BookingPageLocators.EMAIL_INPUT, keys=EMAIL)
            self.click(*BookingPageLocators.CONFIRM_BUTTON)
            self.click(*BookingPageLocators.END_EXIT_BUTTON)
            self.click(*BookingPageLocators.EXIT_BUTTON)
        except:
            self.click(*BookingPageLocators.IF_FLAT_IS_REQUESTED)

        try:
            self.browser.find_element(By.XPATH,
                                      f'(//td[@style="display: flex;align-items: center;justify-content: center;"])[{fifth_flat}]').click()
            self.click(*BookingPageLocators.REQUEST_BUTTON)
            self.click(*BookingPageLocators.AGREE_RADIO_BUTTON)
            self.send_keys(*BookingPageLocators.NAME_INPUT, keys=FIO)
            self.send_keys(*BookingPageLocators.NUMBER_INPUT, keys=PHONE_NUMBER)
            self.send_keys(*BookingPageLocators.EMAIL_INPUT, keys=EMAIL)
            self.click(*BookingPageLocators.CONFIRM_BUTTON)
            self.click(*BookingPageLocators.END_EXIT_BUTTON)
            self.click(*BookingPageLocators.EXIT_BUTTON)
        except:
            self.click(*BookingPageLocators.IF_FLAT_IS_REQUESTED)
