from selenium.webdriver.common.by import By


class BookingPageLocators():
    NUMBERS_OF_FLATS = (By.XPATH, '(//*[@data-attr="favourite-in-table"])//td[4]')
    SORT_BUTTON = (By.XPATH, '//th[@data-rname="obschPloschad"]')
    SHOW_MORE_BUTTON = (By.XPATH, '//p[@class="text-button text-center"]')
    REQUEST_BUTTON = (By.XPATH, '//button[@class="btn btn-default show-contact"]')
    AGREE_RADIO_BUTTON = (By.XPATH, '//input[@class="custom-checkbox form-control"]')
    NAME_INPUT = (By.XPATH, '//input[@id="contact-name"]')
    NUMBER_INPUT = (By.XPATH, '//input[@id="contact-phone"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="contact-email"]')
    EXIT_BUTTON = (By.XPATH, '(//button[@data-dismiss="modal"])[12]')
    CONFIRM_BUTTON = (By.XPATH, '//button[@id="sndbtncnt"]')
    END_EXIT_BUTTON = (By.XPATH, '//button[@class="swal2-close"]')
    IF_FLAT_IS_REQUESTED = (By.XPATH, '(//button[@class="close"])[2]')