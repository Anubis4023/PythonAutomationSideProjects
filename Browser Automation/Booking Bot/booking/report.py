#File includes a class with instance methods responsible to output the hotels we have found from our search

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, hotels_element:WebElement):
        self.hotels_element = hotels_element
        self.hotels = self.hotels_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        #print(len(self.hotels))

    def get_titles(self):
        for hotel in self.hotels:
            hotelName = hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip()
            print(hotelName)




