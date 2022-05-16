from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 

class BookingReport:
    def __init__(self, driver:WebDriver, hotels_element:WebElement):
        self.driver = driver
        self.hotels_element = hotels_element
        self.hotels = self.hotels_element.find_elements(By.CSS_SELECTOR, 'div[class="result__list-item"]')

    def search(self):
        self.findPrice(self.hotels[0])

        for hotel in self.hotels: #for each hotel, click on booking, get redirected, get price, close tab, 
                                  #go back to first tab, apply filters again (make it one function), 
                                  #and continue process for every hotel using findPrice on each one
            pass

    def findPrice(self, hotel:WebElement):
        #Press button to get redirected to hotel booking
        hotelBooking = hotel.find_element(By.CSS_SELECTOR, 'button[class="mod--cta-fullbg mod--cta-full-width mod--cta-color-red booking-button-JS"]')
        hotelBooking.click()

        #Press the 'Booking' button to begin booking for the hotel
        booking_button = self.driver.find_element(By.ID, 'hotelinfo_cta_booking')
        #booking_button.click()

