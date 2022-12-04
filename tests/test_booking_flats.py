from pages.booking_page import BookingPage
from conf import BOOKING_PAGE_URL

def test_booking_page(browser):
    booking_page = BookingPage(browser, BOOKING_PAGE_URL)
    booking_page.open()
    booking_page.should_be_booking_page()

    booking_page.get_all_numbers_of_flats()